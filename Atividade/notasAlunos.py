import json
import os

aluno = 'dados.json'

def carregarDados():
    try: 
        with open(aluno, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def salvarDados(dados):
    with open(aluno, 'w', encoding='utf-8') as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)

    
def validarNota(nota):
    return 0.0 <= nota <= 10.0

#escolha de numero 1
def cadastroAluno(dados):
    try:
        qtd = int(input("Quantos alunos quer cadastrar: "))
    except ValueError:
        print("Numero invalido, tente novamente!")
        return

    for i in range(qtd):
        nome = input("Nome do aluno: ").strip()
        if nome in dados:
            print("Aluno já cadastrado")
            continue  

        try:
            nota1 = float(input("Nota1: "))
            if not validarNota(nota1):
                print("Nota não válida")
                continue
        except ValueError:
            print("Nota incorreta, tente novamente")
            continue

        try:
            nota2 = float(input("Nota2: "))
            if not validarNota(nota2):
                print("Nota não válida")
                continue
        except ValueError:
            print("Nota incorreta, tente novamente")
            continue

        try:
            nota3 = float(input("Nota3: "))
            if not validarNota(nota3):
                print("Nota não válida")
                continue
        except ValueError:
            print("Nota incorreta, tente novamente")
            continue

        media = (nota1 + nota2 + nota3) / 3
        if media >= 6:
            print(f"{media:.2f}: Aprovado")
        else:
            print(f"{media:.2f}: Reprovado")

        
        dados[nome] = {
            "Nota 1": nota1,
            "Nota 2": nota2,
            "Nota 3": nota3,
            "Media": media
        }
        salvarDados(dados)
        print(f"\nRegistro de {nome} feito com sucesso.")

    
    if dados:
        maior_media = max(dados.items(), key=lambda item: item[1]['Media'])
        menor_media = min(dados.items(), key=lambda item: item[1]['Media'])

        print(f"\nMaior média: {maior_media[0]} com {maior_media[1]['Media']:.2f}")
        print(f"Menor média: {menor_media[0]} com {menor_media[1]['Media']:.2f}")
        
#escolha de numero 2

def visualizarNota(dados):
    nome = input("Digite o nome do(a) aluno(a): ").strip()
    if nome in dados:
        info = dados[nome]
        print(f"Nome: {nome}")
        print(f"Nota1: {info['Nota 1']}")
        print(f"Nota2: {info['Nota 2']}")
        print(f"Nota3: {info['Nota 3']}")
        print(f"Média: {info['Media']}")

    else:
        print("Aluno(a) não cadastrado") 


#escolha de numero 3

def removerAluno(dados):
    nome = input("Escreva o nome do aluno(a) para deletar: ").strip()
    if nome in dados:
        del dados[nome]
        salvarDados(dados)
        print("Aluno(a) removido com sucesso!")
    else:
        print("Aluno(a) ja deletado ou não cadastrado")


#tela de menu

def menu():
    dados = carregarDados()
    while True:
        print("\n __Menu__")
        print("1- Adicionar aluno(a)/ver media")
        print("2- visualizar aluno(a)")
        print("3- Remover aluno(a)")
        print("4- sair")

        try:
            opcao = int(input("Escolha um numero: "))
        except ValueError:
            print("Digite um número válido!")
            continue

        match opcao:
            case 1:
                cadastroAluno(dados)
            
            case 2:
                visualizarNota(dados)

            case 3:
                removerAluno(dados)

            case 4:
                print("Saindo. . .")
                break

            case _:
                print("Opção invalida!")
        

if __name__ == "__main__":
    menu()



