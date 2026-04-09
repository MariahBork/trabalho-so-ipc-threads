with open("flores.pgm", 'rb') as f:
    f.readline()  # P5
    linha = f.readline().strip()
    while linha.startswith(b'#'):
        linha = f.readline().strip()
    largura, altura = map(int, linha.split())
    maxval = int(f.readline().strip())
    pixels = f.read()

print(f"Largura: {largura}")
print(f"Altura: {altura}")
print(f"Total de pixels: {len(pixels)}")
print(f"Tamanho aproximado: {largura * altura / 1024:.1f} KB")