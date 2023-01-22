from random import randint

nome = ('pedra','papel', 'tesoura')

nome1 = randint(0,2)
print('''[0] pedra
[1] papel
[2] tesoura''')
jog = int(input('qual sua jogada:'))
print(f'computador jogou {nome[nome1]}')
print(f'jogador jogou {nome[jog]}')

if nome1 == 0:
    if jog == 0:
        print('empatou')
    elif jog == 1:
        print('jogador vence ')
    elif jog == 2:
        print('computador vence')
    else:
        print('opcao invalida')

if nome1 == 1:
    if jog == 0:
        print('computador vence')
    elif jog == 1:
        print('empatou ')
    elif jog == 2:
        print('jogador vence')
    else:
        print('opcao invalida')
if nome1 == 2:
    if jog == 0:
        print('computador vence')
    elif jog == 1:
        print('jogador vence ')
    elif jog == 2:
        print('empatou')
    else:
        print('opcao invalida')


