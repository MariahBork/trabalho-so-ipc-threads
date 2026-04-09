def ler_pgm(caminho):
    with open(caminho, 'rb') as f:
        # Ler cabeçalho
        formato = f.readline().strip()
        # Pular comentários (se houver)
        linha = f.readline().strip()
        while linha.startswith(b'#'):
            linha = f.readline().strip()
        largura, altura = map(int, linha.split())
        maxval = int(f.readline().strip())
        
        # Ler os pixels
        pixels = f.read()
        
        print(f"Formato: {formato}")
        print(f"Largura: {largura}, Altura: {altura}")
        print(f"Valor máximo: {maxval}")
        print(f"Total de pixels: {len(pixels)}")
        print(f"Primeiros 10 pixels: {list(pixels[:10])}")
        
        return largura, altura, maxval, pixels

if __name__ == "__main__":
    ler_pgm("imagem_teste.pgm")