#Exercício Python 13: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento
n = float (input('Digite seu salário: '))
salario = n * 1.15
print('Parabéns você recebeu um aumento! seu novo salário é: {:.2f} '.format(salario))