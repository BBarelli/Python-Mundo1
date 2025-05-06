#Exercício Python 10: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
n = float(input('Qual o seu saldo:R$ '))
dolar = (n / 5.70) #valor do dolar em 06/05/2025
print('O saldo utilizado de R$ {:.2f}, equivale a US {:.2f}'.format(n, dolar))
