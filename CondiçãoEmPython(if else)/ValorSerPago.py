valor = int(input('Digite o valor do produto: '))

des10 = valor - ((valor / 100) * 10)
des5 = valor - ((valor / 100) * 5)
juros = ((valor / 100) * 20) + valor
valores = juros / 3

print('=-=-=-=-=-=-=-=-=-=-=-=-=-')
print('1 - Pagamento á vista Dinheiro/cheque com 10% de desconto: ')
print('2 - Pagamento cartão 5% de desconto: ')
print('3 - Pagamento 3x ou mais no cartão de credito com adicional de 20% do valor do produto: ')
pagamento = int(input('Digite a forma de pagamento: '))
print('=-=-=-=-=-=-=-=-=-=-=-=-=-')

if pagamento == 1:
    print('Voce vai pagar {} reais.'.format(des10))
elif pagamento == 2:
    print('Voce vai pagar {} reais.'.format(des5))
elif pagamento == 3:
    print('Voce vai pagar {} reais. E a parcela sera R${}'.format(juros, valores))

else:
    print('Comando invalido!')

