from collections import Counter

frase = input(f"escreva uma frase: ")
frase = frase.lower()
frase = ''.join(c for c in frase if c.isalpha())

contagem = Counter(frase)

for letra, qtd in contagem.items():
    if qtd > 1:
        print(f'a letra {letra} se repete: {qtd}')
