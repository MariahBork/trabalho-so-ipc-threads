# Cria uma imagem PGM gradiente 512x512 para testes de desempenho
largura, altura = 512, 512
print(f"Criando imagem gradiente {largura}x{altura}...")

with open("gradiente.pgm", "wb") as f:
    f.write(f"P5\n{largura} {altura}\n255\n".encode())
    for i in range(altura):
        for j in range(largura):
            # Padrão gradiente diagonal
            valor = (i + j) % 256
            f.write(bytes([valor]))

print("✅ Imagem gradiente.pgm criada com sucesso!")
print(f"Tamanho do arquivo: {largura * altura} pixels")