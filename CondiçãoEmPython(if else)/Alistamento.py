import datetime
ano = datetime.datetime.now().year
nascimento = int(input('Digite seu ano de nascimento: '))

alistamento = ano - nascimento
print('Voce tem {} anos.'.format(alistamento))

falta = (nascimento / nascimento) * 12
meses = alistamento * 12

print('Vai alistar no serviço militar:')
alistar = int(input('(1 - SIM / 2 - NÃO): '))

if alistar == 1:
    print('Muito bem!')
elif alistar == 2:
    print('Saiba que o serviço militar para jovens acima de 18 anos é obrigatorio.')
else:
   print('Comando invalido!')

if alistamento >= 18:
   print('Já esta na hora de se alistar!')
else:
   print('Ainda não esta na hora de se alistar, falta {} meses para seu alistamento!'.format(meses))






