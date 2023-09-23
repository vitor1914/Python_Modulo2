import random

contador = 0
number = random.randint(1, 10)

while True: #while True para que o jogo continue até que o jogador adivinhe o número correto
    n = int(input('Digite um número de 1 a 10: '))
    contador += 1

    if number == n:
        print('Você ganhou!')
        break #e, em seguida, ele quebre o loop com break.
    else:
        print('Tente novamente.')

print('Foram {} tentativas para você ganhar.'.format(contador))



