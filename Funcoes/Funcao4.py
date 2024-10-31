import random

def game(numero):
    player2 = random.randint(0,5)
    if (numero + player2) % 2 == 0:
        return 'PAR - player1 venceu'
    
    else:
        return 'ÍMPAR - player2 venceu'


print('~'*40)
print('jogo - par ou ímpar')
print('números permitidos - 0, 1, 2, 3, 4 ou 5')
print('~'*40)

jogadas = int(input('quantas vezes você deseja jogar?: '))
for i in range(jogadas):

    player1 = int(input('escolha sua jogada: '))
    print(f' {game(player1)}')

