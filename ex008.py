#Exercício Python 8: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
n = int(input('Digite quantos metros deseja calcular: '))
c = n * 100
m = n * 1000
print('A metragem informada {} M, em centimetros será {}cm e em milimetros {}mm'.format(n, c, m))