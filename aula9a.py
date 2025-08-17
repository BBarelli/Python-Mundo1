'''
SOBRE STRING VEREMOS - (FATIAMENTO / ANALISE / DIVISAO / TRANSFORMAÇÃO)

#FATIAMENTO DE STRING
Exemplo: frase = 'Curso em Video Python - Totalizando 21 indice (letras)

Exibindo somente um indice:
print((frase[9]))

Caso queira pegar o intervalo de indices:
print((frase [9:13]))

ATENÇÃO!!! o valor informado no final do intervalo mostrará um número a menos do que foi informado
No caso acima o que irá ficar visivel é do 9 a 12

Outro exemplo é pulado as letras
Frase[9:21:2] (inicio: 9, fim: 21, passo: 2)
*ele ira pular 2 casas até mostrar a próxima letra

Mas uma maneira
Frase[:5]
*quando não informamos o valor de inicio, ele começa pelo indice zero

Outra maneira
Frase[9::3]
*Inicia na casa 9, não tem indice final e vai pulando de 3 em 3 
_______________________________________________________________________________

#ANALISE
@length - sign. comprimento (No Python só 'len')
ex: print(len(frase))
21 caracteres

@'count' sign. (contar)
*ex: print(frase.count('o'))
Está pedindo pra contar quantas vezes a letra 'o' aparece

uma outra maneira é fazer uma CONTAGEM + FATIAMENTO
*ex: frase.count('o',0,13)

@'find' sign. (encontrar)
*ex: print(frase.find('deo'))

@'in' sign. (entre)
'Curso' in frase
A resposta é True ou False, nesse caso é True

frase = "Curso em Vídeo Python"
resultado = 'Curso' in frase
print(resultado)
_____________________________________________________________________________

#TRANSFORMAÇÃO

@REPLACE - trocar, substituir
ex: frase.replace('Python','Android')

@UPPER - pra cima (metodo)
ex: frase.upper()

@LOWER - pra baixo (metodo)
ex: frase.lower()

@CAPITALIZE() - em uma frase ele joga todos os caracteres pra minusculo, exceto a primeira letra que permanece Maiuscula 
ex: frase.capitalize()

@TITLE - Faz um papel parecido com o capitalize porém ele conta as palavras em uma frase e coloca em maisucula a primeira letra de cada palavra
ex: frase.title()

@STRIP() - remove todos os espaçoes desnessários da string
ex: frase.stip()
**RSTRIP - remove os espaços a direita da frase
**LSTRIP - remove os espaços a esquerda da frase
_____________________________________________________________________________

#DIVISÃO
{ESTUDAR!!: COMO FAZER UM SPLIT}

@SPLIT() - vai divir uma string em uma lista onde cada elemento será separado por espaço
ex: frase.split()

@'-'JOIN - vai juntar uma string onde cada elemento era separado por espaço
ex: '-'join(frase) ('-' simbolo separador)

palavras = ["Python", "é", "incrível"]
resultado = ' '.join(palavras)
print(resultado)
'''
