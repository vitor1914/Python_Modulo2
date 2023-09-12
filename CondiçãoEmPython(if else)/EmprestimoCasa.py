valor = float(input('Valor da casa: '))
salario = float(input('Qual é o salario: '))
anos = int(input('Quantos anos ele deve pagar: '))

meses = anos * 12
pres = valor / meses
exec = (salario / 100) * 30

if pres >= exec:
    print('Não pode financiar')
else:
    print('Pode financiar')