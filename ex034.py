'''Exercício Python 34: Escreva um programa pergunte o salário de um funcionário e calcule o valor do seu aumento
1. Para salários superiores a 1.250,00 calcule um aumento de 10%
2. Para os inferiores ou iguais, o aumento é de 15%'''

salario = float(input('Digite seu salario: '))
#condição
if salario >= 1250:
    novosalario = salario + (salario * 10 / 100)
    print('Com base no valor de R$ {:.2f} você teve um aumento! Seu novo salário será de: R$ {:.2f}'.format(salario, novosalario))
else:
    salario = salario + (salario * 15 / 10)
    print('Com base no valor de R$ {:.2f} você teve um aumento! Seu novo salário será de: R$ {:.2f}'.format(salario, novosalario))


