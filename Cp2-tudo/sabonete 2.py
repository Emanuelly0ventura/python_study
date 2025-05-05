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