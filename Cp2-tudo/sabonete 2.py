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

#abrir json
import json

with open ('data.json', 'r') as file: #para leitura
    data = json.load(file)

with open ('output.json', 'w') as file: # para escrita
    json.dump(data, file)


    print(input("1-Ler e apresentar os dados do arquivo JSON \n" +
"2-Criar novos registros \n" +
"3-Remover registros \n"+
"4-Alterar (idade, sexo, cidade, estado) de uma pessoa \n" +
'5-Listar todas as pessoas de um estado - digito o estado e mostra a lista \n'+
"6-Sair do programa \n" ))
    
arquivos = 'dados.json'
estados = (
    'AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO',
    'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI',
    'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO'
)


