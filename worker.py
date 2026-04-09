import time
import struct

PIPE_FILE = r"C:\Users\maria\trabalho_so\meu_pipe.txt"

def main():
    print("Worker: Aguardando imagem...")
    
    while True:
        try:
            with open(PIPE_FILE, 'rb') as f:
                dados = f.read()
                if dados:
                    print(f"Worker: Recebidos {len(dados)} bytes")
                    break
        except FileNotFoundError:
            pass
        time.sleep(0.1)
    
    # Ler cabeçalho: 12 bytes (3 inteiros de 4 bytes cada)
    cabecalho = dados[:12]
    pixels = dados[12:]
    
    largura, altura, maxval = struct.unpack('III', cabecalho)
    
    print(f"Worker: Imagem {largura}x{altura}, maxval={maxval}")
    print(f"Worker: Pixels esperados: {largura * altura}")
    print(f"Worker: Pixels recebidos: {len(pixels)}")
    
    # Salvar imagem
    with open("imagem_recebida.pgm", 'wb') as f:
        f.write(f"P5\n{largura} {altura}\n{maxval}\n".encode())
        f.write(pixels)
    
    print("Worker: Imagem salva como 'imagem_recebida.pgm'")

if __name__ == "__main__":
    main()