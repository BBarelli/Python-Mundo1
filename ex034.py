'''Exercício Python 34: Escreva um programa pergunte o salário de um funcionário e calcule o valor do seu aumento:
1. Para salários superiores a 1.250,00 calcule um aumento de 10%
2. Para os inferiores ou iguais, o aumento é de 15%'''

salario = float(input('Digite o valor do seu salario: '))
sminimo = 1250.00
nvsalario10 = salario * 1.10
nvsalario15 = salario * 1.15

#condição
if salario > sminimo:
    salario = nvsalario10
    print('Seu salário com aumento passara a ser {:.2f}'.format(salario))
else:
    salario = nvsalario15
    print('Seu salario com aumento passara a ser {:.2f}'.format(salario))
    


