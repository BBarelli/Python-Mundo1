#Exercício Python 30: Crie um programa que leia um número inteiro e mostre na tela se é par ou ímpar

n = int(input('Digite um número: ')).strip()
#Calculo montado para pegar o 'resto' da divisão
x = n % 2
print('Ele é par.' if x == 0 else 'Ele é ímpar.')


