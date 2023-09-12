num1 = int(input('Digite um número: '))
num2 = int(input('Digite um número: '))

if num1 > num2:
    print('Número {} é maior que {}'.format(num1, num2))
elif num1 < num2:
    print('Número {} é maior que {}'.format(num2, num1))
else:
    print('Os numeros são iguais!')