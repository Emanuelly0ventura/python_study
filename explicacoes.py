# 1 numero inteiro com zeros à esquerda

num_int = 10
print(f'{num_int:05d}') #0010

#2 numero float formatado com duas casas

num_float = 3.141
print(f"{num_float: .2f}")
print(f"{num_float: .4f}")


#3 numero formatados com tamanho 5

numeros = [10, 1, 335, 4500]
for num in numeros:
   print(f'{num:5,.0f}' .replace(',','.'))

#4 numero float formatados com duas casas

num1 = 3.14
num2 = 5.876
num3 = 8.9

print(f"{num1:5.2f}" .replace('.',',')) #3,14
print(f'{num2:5.2f}' .replace('.',',')) #5,88
print(f'{num3:5.2f}' .replace('.',',')) #8,90

num = 3300.98
print(f'{num:,.2f}'.replace(',', 'y').replace('.', ',').replace('y', '.'))

nome = "aula3"

print(f"{nome:<10}")
print(f"{nome:^10}")
print(f"{nome:>10}")