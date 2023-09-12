import random

while True:
    print('================================')
    print('Bem-vindo!')
    print('Pedra, Papel e Tesoura!')
    print('================================')
    print('1 - Pedra')
    print('2 - Papel')
    print('3 - Tesoura')

    num = int(input('Digite um número para jogar (ou 0 para sair): '))

    if num == 0:
        print('Obrigado por jogar! Até a próxima!')
        break  # Encerra o jogo se o usuário escolher sair.

    numero_aleatorio = random.randint(1, 3)

    if num == 1 and numero_aleatorio == 3:
        print('Pedra ganhou! Você ganhou!')
    elif num == 3 and numero_aleatorio == 1:
        print('Pedra ganhou! Você perdeu!')
    elif num == 1 and numero_aleatorio == 2:
        print('Papel ganhou! Você perdeu!')
    elif num == 2 and numero_aleatorio == 1:
        print('Papel ganhou! Você perdeu!')
    elif num == 3 and numero_aleatorio == 2:
        print('Tesoura ganhou! Você ganhou!')
    elif num == 2 and numero_aleatorio == 3:
        print('Tesoura ganhou! Você perdeu!')
    else:
        print('Comando inválido!')





