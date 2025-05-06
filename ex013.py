#Exercício Python 13: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salario = float(input('Digite o valor do seu salário: R$ '))
novo = salario + (salario * 15 / 100)
print('Seu sálario no valor de R$ {:.2f}, com o aumento de 15% passa a ser no valor de R${:.2f}'.format(salario, novo))