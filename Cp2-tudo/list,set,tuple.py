#aula q eu entendi nada

#list = [] mudavel e coloca ordem - duplicar OK
#set = {} sem ordem e inalterável - add / remover OK mas duplicar NÂO
#tuple = () mudavel e inalterável - duplica OK so q mais rapido

frutas = ("maça", "abacaxi", "morango", "banana")

frutas[0]

print(len(frutas))
print("abacaxi" in frutas)

for i in (0,1,2,3):
    print(frutas[i])

#ESSES SÃO UTILIZADOS EM LIST

#frutas.clear - limpa lista
#frutas[0] = "pera" - substitui a possição q escolher
#for futa in frutas:print(futa) - deixa em ordem
#frutas.insert(0, "pera") - adiciona na frente
#frutas.append("sopa") - add  
#frutas.sort --> classifica
#so se usa se os tipos são iguas
#frutas.reverse --> inverte
#print(len(frutas)) - quantidade de itens

#ESSES SÃO UTILIZADOS EM SET

#set n repete itens
#frutas.insert(0, "pera") - adiciona na frente
#frutas.append("sopa") - add  
#frutas.sort - classifica
#frutas.add("pera") - adiciona na lista de forma aleatoria(pelo oq eu entendi)
#frutas.remove("banana") - remove item selecionado da lista
#frutas.pop() - remove qualquer elemento aleatorio
#frutas.clear - limpa lista
#print(len(frutas)) - quantidade de itens


#ESSES SÃO UTILIZADOS EM TUPLES

#tuples deixa repetir itens
#print(dir(frutas))
#for futa in frutas:print(futa) - deixa em ordem
#frutas.clear - limpa lista
#print(len(frutas)) - quantidade de itens
#print(index(frutas)) - quantidade de um mesmo itens na index(?)
#print(frutas.count("banana")) - fala a quantidades de um mesmo item em uma lista



#frutas.clear - limpa lista
#frutas[0] = "pera" - substitui a possição q escolher
#for futa in frutas:print(futa)
#frutas.insert(0, "pera") - adiciona na frente
#frutas.append("sopa") - add  
#frutas.sort --> classifica
#so se usa se os tipos são iguas
#frutas.reverse --> inverte

print(frutas)