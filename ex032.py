#Exercício Python 32: Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTOAdd commentMore actions

ano = int(input('Digite um ano, e direi se é bissext ou não: '))
b = ano
ano = int(input('Digite um ano, e direi se é bissexto ou não: '))

# A divisão por 4 com resto ZERO
if ano % 4 == 0 and ano % 100 != or ano % 400 == 0:
    print('O ano é BISSEXTO.')
else:
    print('O ano não é BISSEXTO.')