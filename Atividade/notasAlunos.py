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
    if 0.0 > nota >= 10.0:
        return True
    return False



#nume 1
def cadastroAluno(dados):
    
    nome = input("Nome do aluno: ").strip()
    if nome in dados:
        print("Aluno ja cadastrado")
        return

    try:
        nota1 = input("Nota1: ")
        if nota1 != validarNota:
            print("Nota não valida")
    except ValueError:
        print("Nota incorreta, tente novamente")

    try:
        nota2 = input("Nota1: ")
        if nota2 != validarNota:
            print("Nota não valida")
    except ValueError:
        print("Nota incorreta, tente novamente")

    try:
        nota3 = input("Nota1: ")
        if nota3 != validarNota:
            print("Nota não valida")
    except ValueError:
        print("Nota incorreta, tente novamente")


    dados[nome] = {
        "Nota 1": nota1,
        "Nota 2": nota2,
        "Nota 3": nota3
    }

    salvarDados(dados)
    print(f"Registro de {nome} feita com sucesso")


