#Exercício Python 10: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

real = float(input('Qual o saldo da sua carteira? R$ '))
dolar = real / 3.27
print('O seu saldo é R$ {:.2F}, com esse valor é possível comprar em dolar: US {:.2F}'.format(real, dolar))

