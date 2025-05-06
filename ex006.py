#Exercício Python 006: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
n = int (input('Digite um número: '))
d = n * 2
t = n * 3
q = n ** 2
print('O dobro de {} é: {}, o triplo {}, e a raiz quadrada {}'.format(n, d, t, q))