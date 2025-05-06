#Emanuelly Ventura | RM: 562339 | Turma:TDSPJ1

import json
import os

#variavel para salvar os dados
usuarios = 'dados.json'

#funções para validar e processar dados

def carregarDados():
    try: 
        with open(usuarios, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def salvarDados(dados):
    with open(usuarios, 'w', encoding='utf-8') as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)

#funções para as varieaveis de idade,

def validarEstado(estado):
    return estado.upper() in estados

def validarIdade(idade):
    if 0 <= idade <= 120:
        return True
    return False

def validarSexo(sexo):
    return sexo.upper() in ('M', 'F')

def criarUsuario(dados):
    
    nome = input("Nome: ").strip()
    if nome in dados:
        print("Usuario já registrado")
        return
    
#atribitos principal

    try:
        idade = int(input("Idade: "))
        if not validarIdade:
            return
            print("Idade fora do intervalo ou incorreto!")
    except ValueError:
        print("Idade incorreta, tente novamente!")
        

    sexo = input("Sexo (M/F): ").strip().upper()
    if not validarSexo(sexo):
        print("Sexo incorreto, tente novamente!")
        return

    cidade = input("Cidade: ").strip()

    estado = input("Estado(sigla): ").strip().upper()
    if not validarEstado(estado):
        print("Estado incorreto, tente novamente!")
        return
    
#ligado ao salvar_dados
    dados[nome] = {
        "idade": idade,
        "sexo": sexo,
        "cidade": cidade,
        "estado": estado
    }
    salvarDados(dados)
    print(f"Registro de {nome} criado com sucesso.")

#comandos de execução

def lerDados(dados):
    if not dados:
        print("Nenhum dado registrado")
        return
    for nome, info in dados.items():
        print(f"Nome: {nome}") 
        print(f"Idade: {info['idade']}")
        print(f"Sexo: {info['sexo']}")
        print(f"Cidade: {info['cidade']}")
        print(f"Estado: {info['estado']}. \n")

def removerUsuario(dados):
    nome = input("Digite o nome do usuario para deletar: ").strip()
    if nome in dados:
        del dados[nome]
        salvarDados(dados)
        print("Usuario removido com sucesso")
    else:
        print("Usuario não detectado")

#atributo que repete pq é para alterar
def alterarUsuario(dados):
    nome = input("Digite o nome do usuario para altera-lo: ").strip()
    if nome not in dados:
        print("Usuario não encontrado!")
        return

    try:
        idade = int(input("Nova idade: "))
    except ValueError:
        print("Idade incorreta, tente novamente!")
        

    sexo = input("Novo sexo (M/F): ").strip().upper()
    if not validarSexo(sexo):
        print("Sexo incorreto, tente novamento!")
        

    cidade = input("Nova cidade: ").strip()
    estado = input("Novo estado (UF): ").strip().upper()
    if not validarEstado(estado):
        print("Estado incorreto, tente novamente!")

    dados[nome].update({
        "idade": idade,
        "sexo": sexo,
        "cidade": cidade,
        "estado": estado
    })
    salvarDados(dados)
    print("Registro alterado com sucesso")

#estados  

estados = (
    
    'AC', 'AL', 'AP',
    'AM', 'BA', 'CE',
    'DF', 'ES', 'GO',
    'MA', 'MT', 'MS',
    'MG', 'PA', 'PB',
    'PR', 'PE', 'PI',
    'RJ', 'RN', 'RS',
    'RO', 'RR', 'SC',
    'SP', 'SE', 'TO'
)

def listaEstado(dados):
    estado = input("Digite o estado (sigla): ").strip().upper()
    if not validarEstado(estado):
        print("Estado incorreto, tente novamente!")
        return
    
# Cria uma lista de nomes das pessoas que estão no estado desejado
    encontrados = [nome for nome, info in dados.items() if info['estado'] == estado]
    if encontrados:
        print(f"Pessoas do estado {estado}:")
        for nome in encontrados:
            print(f"- {nome}")
    else:
        print(f"Não há pessoas cadastradas no estado {estado}.")
    
#menu principal 
def menu():
    dados = carregarDados()
    while True:
        print("\nMenu:")
        print("1 - Ler e apresentar os dados")
        print("2 - Criar novos registros")
        print("3 - Remover registros")
        print("4 - Alterar (idade, sexo, cidade, estado) de uma pessoa")
        print("5 - Listar todas as pessoas de um estado")
        print("6 - Sair do programa")

        try:
            opcao = int(input("Escolha um numero: "))
        except ValueError:
            print("numero incorreto, tente novamente!")
            continue

        match opcao:
            case 1:
                lerDados(dados)
            case 2:
                criarUsuario(dados)
            case 3:
                removerUsuario(dados)
            case 4:
                alterarUsuario(dados)
            case 5:
                listaEstado(dados)
            case 6:
                print("Sair")
                break
            case _:
                print("Opção invalida")
                
if __name__ == "__main__":
    menu()


    
        