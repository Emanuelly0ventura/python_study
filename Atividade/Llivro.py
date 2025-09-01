import json
import os

livro = "dados.json"

def carregarDados():
    try:
        with open(livro, 'r',encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def salvarDados(dados):
    with open(livro, 'w', encoding='utf-8') as f:
        json.dump(dados, f, indent=4,ensureascii=False)

#========================

def validarAutor(autor):
    if (1,2,3,4,5,6,7,8,9,0) in autor:
        return False
    return True
    
def validarAno(ano):
    if (1,2,3,4,5,6,7,8,9,0) in ano:
        return True
    return False



#========================

def cadastarLivro(dados):

    id = input("Id: ")
    if id in dados:
        print("Livro ja existe")
        return

    titulo = input("Titulo: ")
    if titulo in dados:
        print("livro ja existe")
        return
    
    try:
        autor = (input("Autor: "))
        if not validarAutor(autor):   
            print("autor inválida")
            return
    except ValueError:
        print("Informação inválida")
        return

    ano = print("Ano de publicação: ")
    if not validarAno(ano):
        print("ano incorreto")
        return 

    dados[id] ={
        "id", id,
        "titulo", titulo,
        "autor", autor,
        "ano", ano
    }

    salvarDados(dados)
    print("Livro cadastrado com sucesso!")

def listaLivros(dados):
    if not dados:
        print("Elementos não encontrados")
    for i in dados.values():
        print(f"Id: {['id']}")
        print(f"Titulo: {['titulo']}")
        print(f"Auto: {['autor']}")
        print(f"Ano: {['ano']}")
        print("--------")

def removerLivro(dados):
    input("Escreva o id para remover o livro: ").strip()
    if id in dados:
        del dados[id]
        salvarDados(dados)
        print("Deletado com sucesso")
    else:
        print("Livro não detectado")
    

def alterarLivro(dados):
    id = input("Digite o ID que queira laterar: ")
    if id not in dados:
        print("Livro não detectado")
        return

    titulo = input("Novo Titulo: ")
    
    try:
        autor = (input("Novo Autor: "))
        if not validarAutor(autor):   
            print("autor inválida")
            return
    except ValueError:
        print("Informação inválida")
        return

    ano = print("Novo Ano de publicação: ")
    if not validarAno(ano):
        print("ano incorreto")
        return 

    dados[id] ={
        "id", id,
        "titulo", titulo,
        "autor", autor,
        "ano", ano
    }

    salvarDados(dados)
    print("Livro cadastrado com sucesso!")


def menu():
    while True:
        dados = carregarDados()
        
            
        print("Menu\n" +
            "1 - cadastrar livro\n" +
            "2 - Lista livro\n" +
            "3 - remover livro\n" +
            "4 - alterar livro\n" +
            "5 - Sair. . .")
        
        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Opção invalida")
            continue

        match(opcao):
            case 1:
                cadastarLivro(dados)
            case 2:
                listaLivros(dados)
            case 3:
                removerLivro(dados)
            case 4:
                alterarLivro(dados)
            case 5:
                break
            case _:
                print("Opção invalida")
    

if __name__ == "main":
    menu()

