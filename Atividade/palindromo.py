palavra = input(f"escreva uma palavra: ")
palavra = palavra.lower()
palavra = ''.join(c for c in palavra if c.isalpha())
palindromo = palavra[::-1]

if palavra == palindromo:
    print(f'{palavra} é um palindromo: {palindromo}')
else:
    print(f'{palavra} não é um palindromo: {palindromo}')
