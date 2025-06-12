#Exercício Python 29: Escreva um programa que leia a velocidade de um carro. 
'''
1. Se ele utrapassar 80km, mostre uma mensagem dizendo que ele foi multado.
2. A multa vai custar R$ 7.00 por cada km acima do limite
'''
v = int(input('Digite a velocidade do carro: '))
vmax = 80
tx  = 7

if v > 80:
    kmacima = v - vmax
    multa = kmacima * 7
    print('Você foi multado, o valor a ser pago é {:.2f}'.format(multa))
    print('Você foi multado, o valor a ser pago é R${:.2f}'.format(multa))
else: 
    print('Velocidade permitida.')
    


