# Aula Variaveis Print Input IF MATCH
# Luiz

x = 0
print(x)
print(type(x))

print(x)
print(x == 0)
if x == 0:
  print("entrou if")
else:
  print("entrou else")
print("terminou")

x = input("digite um numero: ")
print(x, type(x))
x = int(x)
print(x, type(x))
print(x % 2 == 0)

if x == 0:
  print("x é zero")
elif x % 2 == 0:
  print(f"{x} é par")
else:
  print(f"{x} é impar")
print("terminou")

# Solicita a entrada dos números
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
# Calcula a soma e a média
soma = numero1 + numero2
media = soma / 2
# Exibe o resultado
print("A média é:", media)

n = int(input("digite um numero: "))

if n % 2 == 0:
  print(f"{n} é par")
else:
  print(f"{n} é impar")
print("fim")

print(f"{x} é impar")

print(x, "é impar")

print("{} é impar".format(x))

x = int(input("digite um numero: "))

match x:
  case 1:
    print("x é um")
  case 2:
    print("x é dois")
  case 3:
    print("x é tres")
  case 4:
    print("x é quatro")
  case _:
    print("nenhum valor valido")

ponto = (1, x)
match ponto:
  case (0, 0):
      print("Origem")
  case (x, 0):
      print(f"Está no eixo X em x={x}")
  case (0, y):
      print(f"Está no eixo Y em y={y}")
  case (x, y):
      print(f"Coordenada genérica: ({x}, {y})")
  case _:
      print("Entrada inválida.")

x = 0
y = "0"

if x == int(y):  # Convert 'y' to an integer using int()
  x = x + int(y)
  print("entrou no if")
else:
  print("entrou no else")

print(x)

x = 0
y = "0"

if str(x) == y:  # Convert 'x' to a string using str()
  x = str(x) + y  # Since 'y' is a string, the '+' operator will perform string concatenation.
  print("entrou no if")
else:
  print("entrou no else")

print(x)

x=0
y=0

if x == 0:
  print("if x")
elif y == 0:
  print("elif y")
else:
  print("else x")

x=1
y=0

if x == 0:
  print("if x")
elif y == 0:
  print("elif y")
else:
  print("else x")

x=1
y=1

if x == 0:
  print("if x")
elif y == 0:
  print("elif y")
else:
  print("else x")

nome = 'Python'
print(f'.         1         2.')
print(f'.12345678901234567890.')
print(f'.{nome:<20}.')
print(f'.{nome:>20}.')
print(f'.{nome:^20}.')
print(f'.{"Python":^20}.')
print(f".{'Python':^20}.")

# 4) Números float formatados com duas casas
num1 = 3.14
num2 = 5.678
num3 = 8.9
print(f'|{num1:10.2f}|'.replace('.', ',')) # 3,14
print(f'|{num2:10.2f}|'.replace('.', ',')) # 5,68
print(f'|{num3:10.2f}|'.replace('.', ',')) # 8,90
print('|1234567890|')

print(f'         1         2         3         4')
print(f'1234567890123456789012345678901234567890')
qtd = 3.258
preco = 1230.40
valor_total = qtd * preco
valor_total = int(valor_total * 100) / 100.0
print(f'{"Preço: ":<14}{valor_total:10,.2f}')
ipi = valor_total * 0.1
ipi = int(ipi * 100) / 100.0
print(f'{"IPI: ":<14}{ipi:10,.2f}')
valor_total += ipi
print(f'{"Preço c/IPI: ":<14}{valor_total:10,.2f}')

temp = 3.149
print(f'{temp:.2f}')
print(f'{temp:.3f}')
print(f'{temp:.4f}')

temp = 12.34
print(f'{temp:,.2f}')

temp = 12.34
print(f'{temp:,.2f}'.replace('.', ','))

temp = 1234.5678
print(f'{temp:,.2f}')

temp = 1234.5678

# 1,234.57 se trocar direto . para , fica 1,234,57 e desta forma não daria para trocar a primeira virgula para ponto
# pois ao executar o replace (substituir em inglês) .replace('.', ',') ele iria substituir as duas , por .
# sendo assim, primeiro troca uma para algum outro simbolo, escolhi trocar a , pela letra X
# .replace(',', 'X') resultando 1X234.57
# desta forma agora eu troco o . por ,    .replace('.', ',') resultando 1X234,57
# e então troco o X por .   .replace('X', '.') resultando 1.234,57

print(f'{temp:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.'))