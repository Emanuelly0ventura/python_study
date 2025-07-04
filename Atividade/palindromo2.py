from collections import Counter

frase = input(f'escreva uma frase com palindromos: ')
frase = frase.lower()
frase = frase.split()
frase = ''.join(c for c in frase if c.isalpha())

palindromo = frase[::-1]
apenas_pali = [palavra for palavra in frase if palavra in palindromo]
contagem = Counter(frase)


for palindromo, qtd in contagem.items():
    if palindromo in frase:
        print(f'{palindromo} -> {qtd}x')

    else:
        print('ishi')
    