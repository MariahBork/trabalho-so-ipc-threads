# Valida o filtro de limiarização (slice) com t1=50, t2=100

with open("flores.pgm", 'rb') as f:
    f.readline()  # P5
    linha = f.readline().strip()
    while linha.startswith(b'#'):
        linha = f.readline().strip()
    f.readline()  # maxval
    orig = f.read()[:30]

with open("imagem_processada.pgm", 'rb') as f:
    f.readline()  # P5
    linha = f.readline().strip()
    while linha.startswith(b'#'):
        linha = f.readline().strip()
    f.readline()  # maxval
    proc = f.read()[:30]

print("=== Validação do Filtro de Limiarização (t1=50, t2=100) ===")
print("Original -> Processado")
print("-" * 40)
for i in range(min(len(orig), len(proc))):
    regra = "mantido" if 50 <= orig[i] <= 100 else "virou 255"
    print(f"{orig[i]:3d} -> {proc[i]:3d}  ({regra})")