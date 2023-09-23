n1 = int(input('Digite um valor: '))
n2 = int(input('Digite o segundo numero: '))


print('=============Menu==========')
print('===========Operação========')
print(' 1 - Soma ')
print(' 2 - Multiplicação ')
print(' 3 - Maior ')
print(' 4 - novos numeros ')
print(' 5 - Sair do programa')
print('===========================')


while True:
    n3 = int(input('Digite um numero: '))

    if n3 == 1:
        sm = n1 + n2
        print('A soma {} e {} = {}'.format(n1, n2, sm))
    elif n3 == 2:
        mp = n1 * n2
        print('A multiplicação de {} * {} = {}'.format(n1, n2, mp))
    elif n3 == 3:
        if n1 > n2:
            print('O numero {} é maior que {}'.format(n1, n2))
        else:
            print('O numero {} é maior que {}'.format(n2, n1))
    elif n3 == 4:
        n1 = int(input('Digite um valor: '))
        n2 = int(input('Digite o segundo valor: '))
    elif n3 == 5:
        print('Programa finalizado.')
        break
    else:
        print('Opção inválida. Escolha uma opção válida (1 a 5).')

