#Exercício Python 29: Escreva um programa que leia a velocidade de um carro. 
'''
1. Se ele utrapassar 80km, mostre uma mensagem dizendo que ele foi multado.
2. A multa vai custar R$ 7.00 por cada km acima do limite
'''

v = int(input('Digite a velocidade do carro: '))
if v > 80:
    print('Você foi multado!')

