'''Exercício Python 31: Desenvolva um programa que:
pergunte a distância de uma viagem em km
Calcule o preço da passagem, cobrando R$0,50 por km para viagens até 200km
e R$0,45 para viagens mais longa'''


distancia = float(input('Quantos Km possui a viagem?:  '))
limite = 200
p1 = 0.50
p2 = 0.45

if distancia <= limite:
    passagem = distancia * p1
    print('O valor da sua passagem é R$ {:.2f}'.format(passagem))

else:
    passagem = distancia * p2
    print('O valor da sua passagem é R$ {:.2f}'.format(passagem))
