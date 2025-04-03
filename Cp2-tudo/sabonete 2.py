#for in e range
for x in range(1, 11, 2):
    print(x)    #a primeira é o começo a segunda o final e a terceira quantos vc quer pular por numero


credit_card = "1234-5678-9012-3456"

#for x in credit_card:
    #print(x)  

# continue == pular o numero/coisa
# break == para antes que o nunmero/coisa apareça

for x in range(1,21):
  if x == 13:
    break
  else:
    print(x)

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

#aula q eu entendi nada
frutas = ("maça", "abacaxi", "morango", "banana")

frutas[0]

for i in (0,1,2,3):
    print(frutas[i])

#frutas.sort --> classifica
#so se usa se os tipos são iguas
#frutas.reverse --> inverte
cordenadas = [(1,2), (3,4), (5,6)]