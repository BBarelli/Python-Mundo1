# Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:
nome = str(input('Digite seu nome completo: ')).strip()

print('Todas as letras Maiusculas: {}'.format(nome.upper())) 

print('Todas as letra minusculas: {}'.format(nome.lower()))

print('Quantas letras ao todo: {}'.format(len(nome) - nome.count(' ')))

print('Quantas letras tem o primeiro nome: {} '.format(nome.find(' '))) #contando até achar o primeiro espaço

