# Exercício Python 16:Crie um programa que leia um número Real qualquer pelo teclado e mostre sua porção inteira
import math
n = float (input('Digite um número: '))
arred = math.trunc(n)
print('O número digitado {}, tem a parte inteira: {} '.format(n, arred))