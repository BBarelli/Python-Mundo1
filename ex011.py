#Exercício Python 11: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
largura = int (input('Digite quantos metros de largura tem a sua parede: '))
altura = int(input('Digite quantos metros de largura tem sua parede: '))
a = largura * altura
print('A sua área total é de {}m2'.format(a))
l = a / 2
print('Será necessário a quantidade de {}L'.format(l))