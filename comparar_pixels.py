# Compara os primeiros pixels da original e da processada
with open("flores.pgm", 'rb') as f:
    f.readline()
    linha = f.readline().strip()
    while linha.startswith(b'#'):
        linha = f.readline().strip()
    f.readline()  # maxval
    orig = f.read()[:20]

with open("imagem_processada.pgm", 'rb') as f:
    f.readline()
    linha = f.readline().strip()
    while linha.startswith(b'#'):
        linha = f.readline().strip()
    f.readline()  # maxval
    proc = f.read()[:20]

print("Original (primeiros 20 pixels):", list(orig))
print("Processado (primeiros 20 pixels):", list(proc))
print("Soma (orig + proc deve dar 255 cada):", [orig[i] + proc[i] for i in range(len(orig))])