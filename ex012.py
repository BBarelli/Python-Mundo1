#Exercício Python 12: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
n = float (input('Digite o valor do produto: '))
preco = n * 0.95
print('Valor do produto com desconto {}R$'.format(preco))
