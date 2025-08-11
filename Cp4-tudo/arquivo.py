arquivo = open('exemplo.txt')
arquivo.seek
# arquivo.tell
# arquivo.readline
# arquivo.read
x = arquivo.read
# with open ('exemplo.txt' 'r') as arquivo:
#     contendo = arquivo.read


with open ('exemplo.txt', 'r') as arquivo:
    linhas = arquivo.readline(
    print(f'O arquivo contém {len(linhas)} linhas.')
    )

with open('exemplo.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    palavras = conteudo.split()
    print(f"O arquivo contém {len(palavras)} palavras")

texto = input("Difgite o texto a ser salvo no arquivo: ")
with open ('exemplo.txt', 'w')as arquivo:
    arquivo.write(texto)

texto_adicional = input('Digite mais texto para adicionar ao arquivo: ')
with open('exemplo.txt', 'a') as arquivo:
    arquivo.write("\n " + texto_adicional)

with open('exemplo.txt', 'r') as arquivo:
    x = arquivo.read()
    print(x)
