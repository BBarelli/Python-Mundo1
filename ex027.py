#Exercício Python 27: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
n = str (input('Digite seu nome completo: ')).strip()

# O split separa as palavras por espaços.
nome = n.split()
print('Muito prazer em te conhecer!')

print('Seu primeiro nome é: {}'.format(nome[0]))

#Foi feito um len pra contar os as palavras em nome.
print('Seu último nome é: {}'. format(nome[len(nome)-1])) 