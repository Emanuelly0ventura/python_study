import json
import os

usuarios = 'dados.json'


def CarregarDados():
    try:
        with open(usuarios, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:   # corrigido
        return {}


def SalvarDados(dados): 
    with open(usuarios, 'w', encoding='utf-8') as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)


#============= Validações ===============

def validarIdade(idade):
    return 0 < idade <= 120
    
def validarEmail(email: str) -> bool:
    if "@" in email and "." in email.split("@")[-1]:  # corrigido
        return True
    return False
    

#========== Ações do menu ============

def CadastrarUsuario(dados):   # corrigido nome
    nome = input("Nome: ").strip()   # corrigido
    if nome in dados:
        print("Usuário já cadastrado")
        return
    
    try:
        idade = int(input("Idade: "))
        if not validarIdade(idade):   
            print("Idade inválida")
            return
    except ValueError:
        print("Informação inválida")
        return
    
    email = input("Email: ").strip().lower()
    if not validarEmail(email):
        print("Email inválido")
        return
    
    dados[nome] = {
        'nome': nome,
        'idade': idade,
        'email': email
    }

    SalvarDados(dados)
    print("Registro salvo com sucesso!")


def ListaUsuario(dados):
    if not dados:
        print("Nenhum usuário cadastrado.")
        return
    
    for u in dados.values():   # corrigido
        print(f"Nome: {u['nome']}")
        print(f"Idade: {u['idade']}")
        print(f"Email: {u['email']}")
        print("----")


def AtualizarUsuario(dados):
    print("opa (aqui você vai implementar atualização)")


def AlterarUsuario(dados):
    print("opa (aqui você vai implementar alteração de contato)")
        

#================== Menu ==================
def Menu():
    dados = CarregarDados()
    while True:
        print("______MENU______")
        print("1 - Cadastrar novo usuário")
        print("2 - Listar usuários")
        print("3 - Atualizar um usuário existente")
        print("4 - Alterar contato")
        print("0 - Sair")

        try:
            opcao = int(input('Escreva o número aqui: '))   
        except ValueError:
            print("Valor errado")
            continue

        match opcao:
            case 1:
                CadastrarUsuario(dados)
            case 2:
                ListaUsuario(dados)
            case 3:
                AtualizarUsuario(dados)
            case 4:
                AlterarUsuario(dados)
            case 0:
                print("Saindo . . .")
                break
            case _:
                print("Opção inválida!")   


if __name__ == "__main__":
    Menu()


             
         
              
        
      
    
