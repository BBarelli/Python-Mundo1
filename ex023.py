# Exercício Python 23: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados
numero = (input('Digite seu número: '))

print ('Unidade:', numero[3])
print('Dezena: ', numero[2])
print('Centena: ', numero[1]) 
print('Milhar: ', numero[0])