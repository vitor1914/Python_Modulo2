num = int(input('Digite um numero: '))

binario = format(num, 'b')

numero_decimal = num
numero_octal = oct(numero_decimal)

decimal_number = num
hexadecimal_string = hex(decimal_number)

print('-=-=-=-=-=-=-=-=-=-=-=-')
print('Digite a base de conversão númerica:')
print('1 = Binario')
print('2 = Octal')
print('3 = Hexadecimal')
print('-=-=-=-=-=-=-=-=-=-=-=-=')

base = str(input('Qual base de conversão? '))

if base == '1':
    print(f'O número binário é: {binario}')
elif base == '2':
  print('Seu numero octal é {}'.format(numero_octal))

elif base == '3':
    print('Seu numero hexadecimal é {}'.format(hexadecimal_string))

else:
  print('Comando invalido')





