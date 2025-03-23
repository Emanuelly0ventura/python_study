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
