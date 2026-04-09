from PIL import Image
import numpy as np

def pgm_para_png(entrada_pgm, saida_png):
    # Ler o arquivo PGM
    with open(entrada_pgm, 'rb') as f:
        # Pular cabeçalho
        f.readline()  # P5
        linha = f.readline().strip()
        while linha.startswith(b'#'):
            linha = f.readline().strip()
        largura, altura = map(int, linha.split())
        maxval = int(f.readline().strip())
        pixels = f.read()
    
    # Converter para array numpy
    img_array = np.frombuffer(pixels, dtype=np.uint8).reshape(altura, largura)
    
    # Salvar como PNG
    img = Image.fromarray(img_array, mode='L')
    img.save(saida_png)
    print(f"Imagem salva como {saida_png}")

if __name__ == "__main__":
    pgm_para_png("imagem_processada.pgm", "imagem_processada.png")