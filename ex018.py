# Exercício Python 18: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo
import math
angulo = int (input('Digite o valor do angulo: '))
#A maioria das funções trigonométricas em Python (e em muitas outras linguagens) trabalha com radianos, não com graus. Isso inclui as funções math.sin(), math.cos(), math.tan() e outras.
# A função math.radians() faz exatamente essa conversão.
