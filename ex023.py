# Exercício Python 23: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados
numero = int((input('Digite seu número: ')))

print ('Unidade:', numero[3])
print('Dezena:', numero[2])
print('Centena:', numero[1]) 
print('Milhar:', numero[0])
# O codígo acima funciona, porém em caso de digitação de 3 números ele dará erro

#Modelo Guanabara

numero = int(input('Digite seu número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('O número informado {}, tem:'.format(numero))
print('Unidade:{}'.format(u))
print('Dezena:{}'.format(d))
print('Centena:{}'.format(c))
print('Milhar:{}'.format(m))
