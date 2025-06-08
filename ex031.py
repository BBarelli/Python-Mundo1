'''Exercício Python 31: Desenvolva um programa que:
pergunte a distância de uma viagem em km
Calcule o preço da passagem, cobrando R$0,50 por km para viagens até 200km
e R$0,45 para viagens mais longa'''

distancia = float(input('Quantos Km possui a viagem?:  '))

if distancia <= 200:
    passagem = distancia * 0.50
    print('O valor da sua passagem é R$ {:.2f}'.format(passagem))

else:
    passagem = distancia * 0.45
    print('O valor da sua passagem é R$ {:.2f}'.format(passagem))
