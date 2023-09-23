media = 0
maior_idade = float('-inf')
mulheres_abaixo = 0

for pessoa in range(4):
    nome = str(input("Digite seu nome: "))
    idade = int(input("Digite sua idade: "))
    sexo = str(input("Digite o sexo: (m/f): "))

    media += idade

    if idade > maior_idade:
        maior_idade = idade
        nome_mais_velho = nome

    if sexo == 'f' and idade < 20:
        mulheres_abaixo += 1

media /= 4

print('{} mulheres abaixo de 20 anos.'.format(mulheres_abaixo))
print('A pessoa mais velha é {} com {} anos.'.format(nome_mais_velho, maior_idade))
print('A média de idade das 4 pessoas é {} anos.'.format(media))
