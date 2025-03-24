#Emanuelly ventura nascimento rm562339 | 1TDSPJ | 24/03/2025
#Carolina Nascimento Gonçalves rm564786 | 1TDSPJ | 24/03/2025


erro_venda = False
erro_cupom = False

valor = input("Venda.......................: ")
if (valor.isdigit()):
    if (float(valor) >= 1000): desconto = 0.1
    else: desconto = 0.05
else:
    erro_venda = True

cupom = input("Tem cupom [s]im ou [n]ão?..: ")
if (cupom.lower() == "s" or cupom.lower() == "n"):
    if (cupom.lower() == "s"): cupom_desconto = 50
    else: cupom_desconto = 0
else:
    erro_cupom = True

if(erro_venda == False and erro_cupom == False):
    print(f"Venda........: {float(valor):>8.2f} \n" +
          f"Desconto.....: {float(valor) * desconto:>8.2f} \n" +
          f"Cupom........: {cupom_desconto:>8.2f} \n" +
          f"Venda Final..: {float(valor) - (float(valor) * desconto) - cupom_desconto:>8.2f} \n")
else:
    if(erro_venda == True and erro_cupom == True): print("Valor de venda e escolha de cupom inválida")
    elif(erro_venda == True and erro_cupom == False): print("valor de venda inválido")
    else: print("Escolha de cupom inválida")
