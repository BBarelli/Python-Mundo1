# Exercício Python 4: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
a = input('Digite algo: ')
print('O tipo primitivo é: ',type(a))
print('O tipo é númerico: ',a.isnumeric())
print('O tipo é alfanumerico: ',a.isalpha())
print('O tipo tem espaço: ',a.isspace())
print('O tipo está maiuscula: ',a.isupper())
print('O tipo está minuscula: ',a.islower())
print('O tipo está capitalizado: ',a.istitle())


