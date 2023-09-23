s = ''  
while s != 'M' and s != 'F':
    s = input('Digite seu sexo [M/F]: ').upper()
    if s == 'M':
        print('Você é homem!')
    elif s == 'F':
        print('Você é mulher!')
    else:
        print('Comando inválido! Repita a operação')

