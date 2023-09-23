num = int(input('Digite um numero: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
         print('\033[30m', end='')
    print('{} '.format(c), end='')
print('\n\033[m0 Número {} foi divisivel {}'.format(num,tot))
if tot == 2:
    print('E por isso ele É PRIMO!')
else:
    print('É por isso que ele NÃO É PRIMO!')