# Exercício Python 15: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
km = float (input('Quantos km foram percorrido: '))
dia = int (input('Durante quantos dias o carro foi utiizado: '))
diaria = (dia * 60) + (km * 0.15)
print('O valor a ser pago pelo serviço é de: {:.2f} R$'.format(diaria))