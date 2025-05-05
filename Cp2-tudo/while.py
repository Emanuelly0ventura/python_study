#While

name = input("digite seu nome: ")

while name == "":
    print("Você não escreveu o seu nome")
    name = input("digite seu nome: ")
print(f"ola {name}") 

comida = input("Escreva uma comida que vc goste (pra sair q): ")

while not comida == "q":
    print(f"vc gosta de {comida}")
    comida = input("Escreva outra comida que vc goste (pra sair q): ")

print("tchau :(")