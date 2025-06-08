#Exercício Python 32: Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO
from datetime import date
ano = int(input('Digite o ano e direi se é bissexto ou nao, caso queira analisar o ano atual digite 0: '))
#comando para pegar o ano atual da máquina
if ano == 0:
    ano = date.today().year

#condição completa do ano bissexto
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é bissexto'.format(ano))
else: 
    print('O ano {} não é bissexto'.format(ano))
