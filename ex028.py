''' Exercicio em Python 28: Escreva um programa que faça o computador 'pensar' em um número entre 0 e 5
 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador,
 o programa deverá escrever na tela se o usuário perdeu ou venceu.

#Condição Simplificada
n = int(input('De 0 a 5, em qual número estou pensando: '))
print('Parabéns' if n == 3 else 'O computador venceu')

# Condição composta
n = int(input('De 0 a 5, em qual número estou pensando: '))
if n == 3:
    print('Parabéns, você acertou!')
else:
    print('Que penas tente outra vez.')'''

from random import randint
import time
computador = randint(0, 5)
jogador = int(input('Digite um numero: '))
print('Você.....')
time.sleep(3)
#condição
if jogador == computador:
    print('ACERTOOOOOOOOOU!')
else:
    print('ERROU eu pensei no {} e não no {}'.format(computador, jogador))
