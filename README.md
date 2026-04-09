Trabalho M1 - Sistemas Operacionais (UNIVALI)

Autora: Mariah Bork
Disciplina: Sistemas Operacionais - Engenharia de Computação
Data: 09/04/2026

📌 Descrição do Projeto

Este projeto implementa um sistema de processamento paralelo de imagens utilizando:
- IPC (Comunicação entre Processos) via FIFO (named pipe)
- Threads para processamento paralelo
- Filtros de imagem: negativo e limiarização com fatiamento (slice)

🏗️ Arquitetura
┌─────────────┐ FIFO ┌─────────────┐
│ SENDER │ ──────────────→ │ WORKER │
│ (emissor) │ (meu_pipe) │ (receptor) │
└─────────────┘ └─────────────┘
↓
┌─────────────┐
│ THREADS │
│ (paralelo) │
└─────────────┘

📁 Estrutura do Repositório

| Arquivo | Descrição |
|---------|-----------|
| `sender.py` | Lê imagem PGM e envia pelo FIFO |
| `worker_final.py` | Recebe imagem e aplica filtro com threads |
| `converter.py` | Converte PGM para PNG |
| `comparar_pixels.py` | Valida filtro negativo |
| `validar_slice.py` | Valida filtro de limiarização |
| `flores.pgm` | Imagem de teste original |

🚀 Como Executar

Pré-requisitos
- Python 3.x instalado
- Bibliotecas: `pip install pillow numpy`

Passo a passo

1. Abra o Terminal 1 (Worker):
   ```bash
   cd C:\Users\maria\trabalho_so
   python worker_final.py

2. Abra o Terminal 2 (Sender):
   ```bash
   cd C:\Users\maria\trabalho_so
   python sender.py

3. No Worker, escolha:
- Filtro: 0 (Negativo) ou 1 (Limiarização)
- Parâmetros (se limiarização): t1 e t2
- Número de threads: 1, 2, 4 ou 8

4. Visualize o resultado:
   ```bash
   python converter.py
Depois abra imagem_processada.png

📊 Resultados Obtidos
Filtro Negativo (imagem flores.pgm - 544x360 pixels)
Threads	Tempo (s)
1	0,0141
2	0,0200
3	0,0253
4	0,0158

Filtro Limiarização (t1=50, t2=100)
Threads	Tempo (s)
4	0,0345

Validação do Filtro Negativo
Original: 59 → Processado: 196 → Soma: 255 ✅
Original: 56 → Processado: 199 → Soma: 255 ✅

🛠️ Tecnologias Utilizadas
- Python 3.12.6
- Bibliotecas: threading, struct, PIL, numpy
- FIFO implementado via arquivo (meu_pipe.txt) no Windows

📝 Aprendizados
Durante o desenvolvimento, enfrentei e superei desafios como:
- Adaptação do FIFO para Windows
- Formatação correta do envio de dados com struct.pack
- Overhead de threads em imagens pequenas
- Validação matemática dos filtros

📚 Referências
- Material da disciplina de Sistemas Operacionais - UNIVALI
- Documentação Python: threading, struct
- Formato PGM: http://netpbm.sourceforge.net/doc/pgm.html

👩‍💻 Autora
Mariah Bork - Ciência da Computação - UNIVALI
