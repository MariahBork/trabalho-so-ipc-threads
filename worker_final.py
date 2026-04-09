import time
import struct
import threading
from concurrent.futures import ThreadPoolExecutor

PIPE_FILE = r"C:\Users\maria\trabalho_so\meu_pipe.txt"

# Filtros
MODE_NEG = 0
MODE_SLICE = 1

def aplicar_filtro_negativo(pixels):
    """Aplica filtro negativo: novo = 255 - original"""
    resultado = bytearray(len(pixels))
    for i in range(len(pixels)):
        resultado[i] = 255 - pixels[i]
    return resultado

def aplicar_filtro_slice(pixels, t1, t2):
    """Aplica filtro de limiarização: fora do intervalo vira 255"""
    resultado = bytearray(len(pixels))
    for i in range(len(pixels)):
        if pixels[i] < t1 or pixels[i] > t2:
            resultado[i] = 255
        else:
            resultado[i] = pixels[i]
    return resultado

def processar_bloco(pixels, inicio, fim, resultado, modo, t1=0, t2=255):
    """Processa um bloco de pixels (usado pelas threads)"""
    for i in range(inicio, fim):
        if modo == MODE_NEG:
            resultado[i] = 255 - pixels[i]
        else:  # MODE_SLICE
            if pixels[i] < t1 or pixels[i] > t2:
                resultado[i] = 255
            else:
                resultado[i] = pixels[i]

def processar_com_threads(pixels, num_threads, modo, t1=0, t2=255):
    """Divide o trabalho entre várias threads"""
    tamanho = len(pixels)
    resultado = bytearray(tamanho)
    
    # Calcular quantos pixels cada thread processa
    bloco_tamanho = (tamanho + num_threads - 1) // num_threads
    
    threads = []
    for i in range(num_threads):
        inicio = i * bloco_tamanho
        fim = min(inicio + bloco_tamanho, tamanho)
        
        if inicio >= tamanho:
            break
            
        t = threading.Thread(
            target=processar_bloco,
            args=(pixels, inicio, fim, resultado, modo, t1, t2)
        )
        threads.append(t)
        t.start()
    
    # Esperar todas as threads terminarem
    for t in threads:
        t.join()
    
    return resultado

def main():
    print("=== WORKER COM PARALELISMO ===")
    print("Aguardando imagem do sender...")
    
    # Receber imagem
    while True:
        try:
            with open(PIPE_FILE, 'rb') as f:
                dados = f.read()
                if dados:
                    print(f"Recebidos {len(dados)} bytes")
                    break
        except FileNotFoundError:
            pass
        time.sleep(0.1)
    
    # Ler cabeçalho
    cabecalho = dados[:12]
    pixels = dados[12:]
    largura, altura, maxval = struct.unpack('III', cabecalho)
    
    print(f"Imagem: {largura}x{altura}, {len(pixels)} pixels")
    
    # Menu para escolher o filtro
    print("\n--- Escolha o filtro ---")
    print("0 - Negativo")
    print("1 - Limiarização (slice)")
    modo = int(input("Digite 0 ou 1: "))
    
    t1, t2 = 0, 255
    if modo == MODE_SLICE:
        t1 = int(input("Digite o limite inferior (ex: 50): "))
        t2 = int(input("Digite o limite superior (ex: 100): "))
    
    # Escolher número de threads
    num_threads = int(input("Digite o número de threads (ex: 4): "))
    
    # Medir tempo de processamento
    print(f"\nProcessando com {num_threads} threads...")
    inicio_tempo = time.time()
    
    # Processar a imagem
    resultado = processar_com_threads(pixels, num_threads, modo, t1, t2)
    
    fim_tempo = time.time()
    tempo_total = fim_tempo - inicio_tempo
    
    print(f"Processamento concluído em {tempo_total:.4f} segundos")
    
    # Salvar imagem processada
    nome_saida = "imagem_processada.pgm"
    with open(nome_saida, 'wb') as f:
        f.write(f"P5\n{largura} {altura}\n{maxval}\n".encode())
        f.write(resultado)
    
    print(f"Imagem salva como '{nome_saida}'")

if __name__ == "__main__":
    main()