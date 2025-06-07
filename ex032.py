#Exercício Python 32: Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO

'''
#Maneira 1
ano = int(input('Digite um ano, e direi se é bissexto ou não: '))

# A divisão por 4 com resto ZERO
if ano % 4 == 0:
    print('O ano é BISSEXTO.')
else:
    print('O ano não é BISSEXTO.')

 '''   
# Maneira 2
ano = int(input('Digite o ano e direi se é bissexto ou nao: '))
print('O ano é bissexto.' if ano % 4 == 0 else 'O ano não é bissexto.')
