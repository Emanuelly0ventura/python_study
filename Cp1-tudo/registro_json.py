
import json
import os

ARQUIVO = 'dados.json'
ESTADOS_VALIDOS = (
    'AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO',
    'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI',
    'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO'
)

#utf-8 = é para padronizar letras e simbolos
def carregar_dados():
    try: #para evitar bugs / r = reading
        with open(ARQUIVO, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

#ligado ao dados / w = writing 
def salvar_dados(dados):
    with open(ARQUIVO, 'w', encoding='utf-8') as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)

def validar_estado(estado):
    return estado.upper() in ESTADOS_VALIDOS

#aqui ele reconhece qual é o sexo selecionado
def validar_sexo(sexo):
    return sexo.upper() in ('M', 'F')

def criar_registro(dados):
    nome = input("Nome: ").strip()
    if nome in dados:
        print("Pessoa já registrada.")
        return
    
#atribito principal
    try:
        idade = int(input("Idade: "))
    except ValueError:
        print("Idade inválida.")
        

    sexo = input("Sexo (M/F): ").strip().upper()
    if not validar_sexo(sexo):
        print("Sexo inválido.")
        return

    cidade = input("Cidade: ").strip()

    estado = input("Estado (UF): ").strip().upper()
    if not validar_estado(estado):
        print("Estado inválido.")
        return
#ligado ao salvar_dados
    dados[nome] = {
        "idade": idade,
        "sexo": sexo,
        "cidade": cidade,
        "estado": estado
    }
    salvar_dados(dados)
    print("Registro criado com sucesso.")

#########################################

def ler_dados(dados):
    if not dados:
        print("Nenhum dado registrado.")
        return
    for nome, info in dados.items():
        print(f"Nome: {nome}, Idade: {info['idade']}, Sexo: {info['sexo']}, Cidade: {info['cidade']}, Estado: {info['estado']}")

def remover_registro(dados):
    nome = input("Digite o nome da pessoa a remover: ").strip()
    if nome in dados:
        del dados[nome]
        salvar_dados(dados)
        print("Registro removido com sucesso.")
    else:
        print("Pessoa não encontrada.")


#atributo que repete pq é para alterar
def alterar_registro(dados):
    nome = input("Digite o nome da pessoa a alterar: ").strip()
    if nome not in dados:
        print("Pessoa não encontrada.")
        return

    try:
        idade = int(input("Nova idade: "))
    except ValueError:
        print("Idade inválida.")
        return

    sexo = input("Novo sexo (M/F): ").strip().upper()
    if not validar_sexo(sexo):
        print("Sexo inválido.")
        return

    cidade = input("Nova cidade: ").strip()
    estado = input("Novo estado (UF): ").strip().upper()
    if not validar_estado(estado):
        print("Estado inválido.")
        return

    dados[nome].update({
        "idade": idade,
        "sexo": sexo,
        "cidade": cidade,
        "estado": estado
    })
    salvar_dados(dados)
    print("Registro alterado com sucesso.")


############################
def listar_por_estado(dados):
    estado = input("Digite o estado (UF): ").strip().upper()
    if not validar_estado(estado):
        print("Estado inválido.")
        return

    encontrados = [nome for nome, info in dados.items() if info['estado'] == estado]
    if encontrados:
        print(f"Pessoas do estado {estado}:")
        for nome in encontrados:
            print(f"- {nome}")
    else:
        print("Nenhuma pessoa encontrada nesse estado.")

def menu():
    dados = carregar_dados()
    while True:
        print("\nMENU:")
        print("1 - Ler e apresentar os dados do arquivo JSON")
        print("2 - Criar novos registros")
        print("3 - Remover registros")
        print("4 - Alterar (idade, sexo, cidade, estado) de uma pessoa")
        print("5 - Listar todas as pessoas de um estado")
        print("6 - Sair do programa")

        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Opção inválida.")
            continue

        match opcao:
            case 1:
                ler_dados(dados)
            case 2:
                criar_registro(dados)
            case 3:
                remover_registro(dados)
            case 4:
                alterar_registro(dados)
            case 5:
                listar_por_estado(dados)
            case 6:
                print("Encerrando o programa.")
                break
            case _:
                print("Opção inválida.")

if __name__ == "__main__":
    menu()
