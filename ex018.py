# Exercício Python 18: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo
import math
#A maioria das funções trigonométricas em Python (e em muitas outras linguagens) trabalha com radianos, não com graus. Isso inclui as funções math.sin(), math.cos(), math.tan() e outras.
angulo = int (input('Digite o valor do angulo: '))

# A função math.radians() faz exatamente essa conversão.
angulo_radianos = math.radians(angulo)

#criando os parametros que faram o calculo
seno = math.sin(angulo_radianos)
cosseno = math.cos(angulo_radianos)
tangente = math.tan(angulo_radianos)

#Exibir
print('O valor de seno é: {:.2f}'.format(seno))
print('O valor de cosseno é: {:.2f}'.format(cosseno))
print('O valor da tangente é: {:.2f}'.format(tangente))