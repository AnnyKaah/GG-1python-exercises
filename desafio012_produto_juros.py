print('Descubra a melhor forma de pagamento para seu produto!')
produto = float(input('Qual o preço do produto? R$'))
print('-'*12)
desconto = (produto - (produto*0.10))
econ = produto - desconto
aumento = (produto + (produto*0.08))
juros = aumento - produto
print('O produto custava R${} na promoção com desconto de 5% para pagamentos a vista irá custar R${:.2f}'.format(produto,desconto))
print('Logo, você economiza R${:.2f}'.format(econ))
print('Mas caso você opte por pagar parcelado em 10X no crédito\no produto irá custar R${:.2f}'.format(aumento))
print('Logo, terá um aumento de R${:.2f}'.format(juros))
print('-'*12)