from random import randint
from time import sleep
itens = ('Tesoura', 'Pedra', 'Papel')
computador = randint(0, 2)

print('''Suas opções:
[ 0 ] Tesoura
[ 1 ] Pedra
[ 2 ] Papel''')

jogador = int(input('Qual é a sua jogada? '))

if jogador < 0 or jogador > 2:
    print('JOGADA INVALIDA')
else:
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!')
    print('-='*15+'-')
    print('Computador jogou {}'.format(itens[computador]))
    print('Jogador jogou {}'.format(itens [jogador]))
    print('-='*15+'-')


    if computador == 0 and jogador == 0:
        print('EMPATE')
    elif computador == 0 and jogador == 1:
        print('COMPUTADOR VENCE')
    elif computador == 0 and jogador == 2:
        print('JOGADOR VENCE')


    if computador == 1 and jogador == 0:
        print('COMPUTADOR VENCE')
    elif computador == 1 and jogador == 1:
        print('EMPATE')
    elif computador == 1 and jogador == 2:
        print('JOGADOR VENCE')

    if computador == 2 and jogador == 0:
        print('JOGADOR VENCE')
    elif computador == 2 and jogador == 1:
        print('COMPUTADOR VENCE')
    elif computador == 2 and jogador == 2:
        print('EMPATE')
