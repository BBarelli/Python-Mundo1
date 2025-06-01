''' Exercicio em Python 28: Escreva um programa que faça o computador 'pensar' em um número entre 0 e 5 e peça para o usuário tentar descobrir
qual foi o número escolhido pelo computador, o programa deverá escrever na tela se o usuário perdeu ou venceu.'''

# Condição composta
n = int(input('De 0 a 5, em qual número estou pensando: '))
if n == 3:
    print('Parabéns, você acertou!')
else:
    print('Que penas tente outra vez.')
