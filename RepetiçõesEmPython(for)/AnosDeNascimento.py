import datetime

menores_idade = 0
maiores_idade = 0

ano_atual = datetime.date.today().year

for i in range(7):
    numero = int(input("Digite o ano de nascimento: "))


    if ano_atual - numero < 21:

        menores_idade += 1
        maiores_idade = 7 - menores_idade


print('Temos {} pessoa menor de idade.'.format(menores_idade))
print('Temos {} pessoas maiores de idade.'.format(maiores_idade))




