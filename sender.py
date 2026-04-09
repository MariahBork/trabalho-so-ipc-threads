import struct

PIPE_FILE = r"C:\Users\maria\trabalho_so\meu_pipe.txt"

def ler_pgm(caminho):
    with open(caminho, 'rb') as f:
        # Pular cabeçalho
        f.readline()  # P5
        linha = f.readline().strip()
        while linha.startswith(b'#'):
            linha = f.readline().strip()
        largura, altura = map(int, linha.split())
        maxval = int(f.readline().strip())
        pixels = f.read()
        return largura, altura, maxval, pixels

def main():
    print("Sender: Lendo imagem...")
    largura, altura, maxval, pixels = ler_pgm("flores.pgm")
    
    print(f"Sender: Imagem {largura}x{altura}, {len(pixels)} pixels")
    
    # Formato: largura (4 bytes) + altura (4 bytes) + maxval (4 bytes) + pixels
    cabecalho = struct.pack('III', largura, altura, maxval)
    dados = cabecalho + pixels
    
    print(f"Sender: Enviando {len(dados)} bytes...")
    
    with open(PIPE_FILE, 'wb') as f:
        f.write(dados)
    
    print("Sender: Imagem enviada!")

if __name__ == "__main__":
    main()