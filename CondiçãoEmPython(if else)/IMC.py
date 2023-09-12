peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura em (ex: 1.80): '))

vezes = altura * altura
imc = peso / vezes

if imc <= 18.5:
    print('ABAIXO DO PESO')
elif imc <= 25:
     print('PESO IDEAL')
elif imc <= 30:
  print('SOBREPESO')
elif imc <= 40:
  print('OBESIDADE')
else:
  print('OBESIDADE MORBIDA')