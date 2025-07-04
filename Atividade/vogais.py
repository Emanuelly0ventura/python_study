from collections import Counter

frase = input("Digite uma frase: ")
frase = frase.lower()  
frase = ''.join(c for c in frase if c.isalpha())

vogais = "aeiouAEIOU"
apenas_vogais = [letra for letra in frase if letra in vogais]

print(f'Total de vogais: {len(frase)}')

contagem = Counter(frase)

for letra, qtd in contagem.items():
    if letra in vogais:
        print(f"A letra {letra} aparece {qtd} vezes.")

