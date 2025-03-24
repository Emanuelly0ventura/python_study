erro_venda = False
erro_cupom = False

venda = input('Venda......................: ')
if (venda.isdigit()):
    if (float(venda) >= 1000): desconto = 0.1
    else: desconto = 0.05
else:
    erro_venda = True

cupom = input('Tem cupom,[s]im ou [n]ão?..: ')
if (cupom.lower() == "s" or cupom.lower() == "n"):
    if (cupom.lower() == "s"): cupom_desconto = 50
    else : cupom_desconto = 0
else:
    erro_cupom = True


if (erro_cupom == False and erro_venda == False):
    print("Relatorio \n" + 
          f'Venda........: {float(venda):8.2f} \n' +
          f'Desconto.....: {float(venda) * desconto:8.2f} \n' +
          f'Cupom........: {cupom_desconto:8.2f} \n' + 
          f'Venda Final..: {float(venda) - float(venda) * desconto - cupom_desconto:8.2f}')
elif (erro_cupom == True and erro_venda == False):
    print('Erro com o cupom')
elif (erro_cupom == True and erro_venda == True):
    print('Erro com o cupom e o valor da venda')
else:
    print("Erro com a valor da venda")
