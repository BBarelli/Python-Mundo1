 # FATIAMENTO DE STRING

 '''
 Exemplo: Curso em Video Python
Totalizando 21 indice

Pra mostrar apenas o indice, tem que informar:
Frase[9] mostrara apenas a letra V

mas caso queira pegar o intervalo

Frase [9:13]

ATENÇÃO!!! o valor informado no final do intervalo mostrará um número a menos do que foi informado
No caso acima o que irá ficar visivel é do 9 a 12

Outro exemplo é pulado as letras
Frase[9:21:2]

ele ira pular 2 casas até mostrar a próxima letra

Mas uma maneira
Frase[:5]

quando não informamos o valor de inicio, ele começa pelo indice zero

Outra maneira
Frase[9::3]

Inicia na casa 9, não tem indice final e vai pulando de 3 em 3 

'''

# ANALISE
'''
#len(frase)      ///       len - significa Comprimento
21 caracteres

Outra função

#frase.count('o')
Está pedindo pra contar quantas vezes a letra o aparece

uma outra maneira é fazer uma contagem + fatiamento
#frase.count('o',0,13)

#frase.find('deo')    /// find - significa Encontrar




'''