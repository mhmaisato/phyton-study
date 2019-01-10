#conversor moeda
brl = float(input('quanto tem na carteira, R$:'))
cot = float(input('qual a cotação do dia,R$:'))
usd = brl/cot
print ('com R${:.2f}, você compra USD${:.2f}' .format(brl, usd))
