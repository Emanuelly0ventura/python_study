import json
import os

usuarios = 'dados.json'


def CarrergarDados():
    try:
        with open(usuarios , 'r', enconding='utf-8') as f:
            return json.load(f)
    except FileExistsError:
        return{}
    
def SalvarDados(dados): 
        with open(usuarios , 'w', enconding='utf-8') as f:
            json.dump(dados ,f ,inden=4, ensure_ascii=False)

#=============Validações===============

def validarIdade(idade):
    if 0 < idade < 120 :
        return True
    else:
        return False
    
def validarEmail(email):
    if '@' not in email:
        print("Email invalido!")
        return True
    else:
        return False
    

#==========Escolhar do menu============

def CadastrarUsusario(dados):
    nome= input("Nome").strip
    if nome in dados:
        return print("Usuario ja cadastrado")
    
    try:
        idade=input("Idade: ")
        if not validarIdade(idade):   
            print("Idade invalida")
            return
    except ValueError:
        print("Informação invalida")
        return
    
    try:
        email=input("Email: ").strip().upper()
        if not validarEmail(email):
            print("Email invalido")
            return
    except ValueError:
        print("Informação invalida")
        return
    
    dados[nome] = {
        'nome': nome,
        'idade': idade,
        'email': email
    }

    SalvarDados(dados)
    print("Registro salvo com sucesso!")

def ListaUsuario(dados):
    for u in usuarios:
        print(f"Nome: {u['nome']}")
        print(f"Idade: {u['idade']}")
        print(f"Email: {u['email']}")

        

#Menu
def Menu():
    dados = CarrergarDados()
    while True:
        print("______MENU______")
        print("1 - Cadastrar novo usuário")
        print("2 - Listar usuários")
        print("3 - Atualizar um usuário existente")
        print("4 - Remover um usuário")
        print("0 - Sair")

        opcao = input(f'Escreva o numero aqui: ')

        match opcao:
            case 1:
                CadastrarUsusario(dados)
            case 2:
                ListaUsuario(dados)
            case 3:
                AtualizarUsuario(dados)
            case 4:
                print("Saindo . . .")
                break
            case _:
                print("Opção invalida!")   

if __name__ == "__main__":
    Menu()

             
         
              
        
      
    
