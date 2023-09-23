import datetime
ano = datetime.datetime.now().year

nascimento = int(input('Digite o ano de nascimento: '))

idade = ano - nascimento

if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JUNIOR')
else:
    print('MASTER')