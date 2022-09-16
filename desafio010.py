real = float(input('Quanto dinheiro você tem na carteira? R$'))
print('-'*12)
dolar = real/5.29
euro = real/5.29
won = real/0.0038
print('Com R${:.2f} você pode comprar US${:.2f} \nE poderá comprar EUR{:.2f} \ne {:.2f}WON'.format(real,dolar,euro,won))
print('-'*12)