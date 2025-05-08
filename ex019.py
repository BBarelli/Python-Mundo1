# Exercício Python 19: Um professor que sortear um dos seus quatros alunos para apagar o quadro. Faça um progrma que ajude ele, lendo o nome deles e escrevendo o nome do escolhido
import random

a1 = input ('Primeiro aluno: ')
a2 = input ('Segundo aluno: ')
a3 = input ('Terceiro aluno: ')
a4 = input ('Quarto aluno: ')
nomes = a1, a2, a3, a4

print(random.choice'O aluno escolhido é: 'format.(nomes))