# Exercício Python 17: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triagulo retangulo, calcule e mostre o comprimento da hipotenusa
# Utilizar o teorema de pitágoras
import math
co = int (input('Digite o comprimento do cateto oposto: '))
ca = int (input('Digite o comprimento do cateto adjacente: '))
hipotenusa = math.hypot(co, ca)
print('O calculo entre o cateto oposto: {} e o cateto adjacente: {} é equivalente a hipotenusa: {}'.format(co, ca, hipotenusa))

