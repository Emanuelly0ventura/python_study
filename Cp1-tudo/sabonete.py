x = input('numero 1: ')
y = input('numero 2: ')

soma = int(x) + int(y)
media = soma/2
print("a média é ",media)

#slide aula2
x = input('nota1: ')
y = input('nota2: ')
a = input('nota3: ')

soma = int(x) + int(y) + int(a)
result = float(soma//3)

print("média é:", result)

x = int(input("valor da compra: "))
y = int(10 % x)
w = int(x - y)
print(f"valor da compra vai dar: ", w)

 #lista 1

a = 5
b = 9
x = not True
y = False and True
m = "casa"
n = "mesa"

print(x and y == x or y)
print(a * b<= b - a)
print(not(a == b or not b != a))
print(not(m != n and b > a))
print(b + a <= a * b and y)
print(x and not y or a // b != a % b)

#slide aula 3

nome = "manu"
idade = 18

print(f"olá, meu nome é {nome} e eu tenho {idade} anos.")

x = 12.895

print(f'{x: .2f}')

texto = "Lorem ipsum dolor sit am"

print(f'{texto:^30}')

#lista de if-elif-else e match

#1
nota = float(input("digite sua nota(notas quebradas com .): "))

if nota >= 9:
 print(f'A')
elif nota >=7:
    print(f'B')
elif nota >=5:
   print(f'C')
else:
   print(f'F')

   #2
num = int(input("digite um numero: "))

if num % 2 == 0:

        print(f'numero par!')
else:
        print(f'numero ímpar!')

#3

peso = float(input("digite seu peso: "))
altura = float(input('digite sua altura: '))
imc = (peso / (altura ** 2))
print(f'seu imc é: {imc: .1f}Kg/M^2')

if imc <18.5:
    print(f'Abaixo do peso')

elif 18.5 < imc < 24.9:
    print(f'Peso nomral')

elif 25 < imc < 29.9:
    print(f'Sobrepeso')

else:
    print(f'Obesidade')
    
#4
print(f'coloque numeros para comparar e ver qual é o maior!')
n1 = input(f'digite o num1: ')
n2 = input(f'digite o num2: ')
n3 = input(f'digite o num3: ')

if n1 > n2 and n1 > n3:
    print(f'n 1 é o numero maior')

elif n3 > n1 and n3 > n2:
        print(f'n 3 é o numero maior')

elif n2 > n1 and n2 > n3:
    print(f'n 2 é o numero maior')

else:
    print(f'ué paizão ta tudo igual')

#5

nt1 = float(input(f'nota 1: '))
nt2 = float(input(f'nota 2: '))
nt3 = float(input(f'nota 3: '))

media = (nt1 + nt2 + nt3)/3

print(f'{media:.1f}')

if media >= 6:
    print(f'aprovado')

else:
    print(f'reprovado')

#6

semi = input(f"digite uma cor do semáforo:")

match semi:
    case "vermelho":
        print(f'pare!')
    case "amarelo":
        print(f'atenção!')
    case "verde":
        print(f'siga!')
    case _:
        print(f'ta louco paaizão????')

#7
print(f"vamos fazer uma operação matematica basica!Digte os numeros:")
operacao = input(f"Digite um operador matematico:")
n1 = float(input(f"numero1: "))
n2 = float(input(f'numero2: '))

match operacao:
    case "+":
        print(f'{n1} + {n2} = {n1 + n2}')
    case "-":
        print(f'{n1} - {n2} = {n1 - n2}')
    case "*":
        print(f'{n1} * {n2} = {n1 * n2}')
    case "/":
        print(f'{n1} / {n2} = {n1 / n2}')    
    case _:
        print(f'paizão é basico')

#8
animal = input(f"Escolah um animal: ")

match animal:
    case "cachorro"|"gato":
        print(f'Mamifero')
    case "cobra"|"largato":
        print(f'Reptil')
    case 'aguia'|"papagaio":
        print(f'Ave')
    case _:
        print(f'Deus sabe eu não')

#9
personagem = input('escolha um numero entre 1 a 3: ')

match personagem:
    case "1":
        print(f"Você escolheu o Guerreiro!")
    case "2":
        print(f"Você escolheu o Mago!")
    case "3":
        print(f"Você escolheu o Arqueiro!")
    case _:
        print(f"Opção invalida!")

#10

nota = input(f"Digite sua nota de 0 a 10: ")

match nota:
    case "9"|"10":
        print(f"A")
    case "7"|"8":
        print(f"B")
    case "5"|"6":
        print(f"C")
    case "3"|"4":
        print(f"D")
    case "0"|"1"|"2":
        print(f"E")