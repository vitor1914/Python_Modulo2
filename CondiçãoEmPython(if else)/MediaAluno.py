nota1 = float(input('Digite a nota 1: '))
nota2 = float(input('Digite a nota 2: '))

soma = (nota1 + nota2) / 2

if soma <= 5:
    print('REPROVADO!')
elif soma == 5:
    print('RECUPERAÇÃO')
elif soma <= 6.9:
    print('RECUPERAÇÃO')
else:
 print('APROVADO!')
