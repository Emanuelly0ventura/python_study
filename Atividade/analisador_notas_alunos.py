### 💻 Atividade de Python - Nível Médio

# 🎯 Desafio: Analisador de Notas dos Alunos

# Objetivo:
# 1. Cadastrar alunos com 3 notas.
# 2. Calcular a média de cada aluno.
# 3. Mostrar aluno com maior e menor média.
# 4. Permitir consulta das notas de um aluno pelo nome.

alunos = []

quantidade = int(input("Quantos alunos deseja cadastrar? "))

for i in range(quantidade):
    print(f"\nAluno {i + 1}:")
    nome = input("Nome: ")
    notas = []
    for j in range(1, 4):
        nota = float(input(f"Nota {j}: "))
        notas.append(nota)
    media = sum(notas) / len(notas)
    alunos.append({"nome": nome, "notas": notas,"media": media})

print("\n--- Médias ---")
for aluno in alunos:
    print(f"{aluno['nome']}: {aluno['media']:.2f}")

maior_media = max(alunos, key=lambda x: x['media'])
menor_media = min(alunos, key=lambda x: x['media'])

print(f"\nMaior média: {maior_media['nome']} ({maior_media['media']:.2f})")
print(f"Menor média: {menor_media['nome']} ({menor_media['media']:.2f})")

nome_busca = input("\nDeseja ver as notas de qual aluno? ")
encontrado = False
for aluno in alunos:
    if aluno["nome"].lower() == nome_busca.lower():
        print(f"Notas de {aluno['nome']}: {aluno['notas']}")
        encontrado = True
        break

if not encontrado:
    print("Aluno não encontrado.")
