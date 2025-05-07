# Aula 8 – Utilizando Módulos
import math # Importar de modo especifico seria o comado (from math import sqrt) - MINUSCULO
n = int (input('Digite um número: '))
raiz = math.sqrt(n)
print('A raiz de {}, é igual a {}'.format(n, raiz)) #pra arred. pra cima/ .format(n, math.ceil(raiz))), pra baixo /.format(n, math.floar(raiz))), pra baixo

#AULA 8 - UTILIZANDO MÓDULOS
#MÓDULOS
#BIBLIOTECAS
# OS PROGRAMAS EM PYTHON POR PADRÃO TEM UM CONJUNTO LIMITADO DE COMANDOS, POR MOTIVO DE AUMENTAR  A VELOCIDADE DA LINGUAGEM, PRA QUE OS PROGRAMAS SEJAM PEQUENOS E NÃO GASTEM TANTA MEMÓRIA.
----------------------------------------------------------------------------------
# DENTRO DA LINGUAGEM PYTHON PRA QUE SEJA INCLUIDO ALGUMA COISA USAR O COMANDO:
#( IMPORT ) OU (FROM IMPORT)

#NO PYTHON VOCÊ DARÁ O COMANDO IMPORT NAS PRIMEIRAS LINHAS DO PROGRAMA, E VAI COLOCAR O NOME DO MÓDULO DA BIBLIOTECA QUE VAI SER CARREGADO PRA ELE.
#IMPORT  = 'NOME DO MÓDULO' 
#ASSIM SERÁ IMPORTADA TODA A BIBLIOTECA:

#MAS CASO EU QUEIRA IMPORTAR ALGO ESPECIFICO DO MÓDULO:
#FROM 'BIBLIOTECA' IMPORT


#EXEMPLO UMA BIBLIOTECA MATEMÁTICA
#TODO O MÓDULO:
#IMPORT MATH

#FUNCIONALIDADE ESPECIFICA:
#FROM MATH IMPORT SQTR - (RAÍZ QUADRADA)
-----------------------------------------------------------------------------------
# COMO EU VEJO AS BIBLIOTECAS QUE POSSO IMPORTAR? 
#-> ACESSAR (https://docs.python.org/3/) - VISUALIZAÇÃO A PARTIR DO SITE OFICIAL

#O ATALHO (IMPORT CNTR + ESPAÇO) LISTA 
-----------------------------------------------------------------------------------
# O AMBIENTE VIRTUAL SERVE PRA CENTRALIZAR AS BIBLIOTECAS EM UM SÓ LUGAR
#COM INSTALAR:
#python -m venv venv

#ENTRAR NO AMBIENTE:
#venv\script\active

# COMO INSTALAR UMA BIBLIOTECA:
#pip install 'biblioteca'
----------------------------------------------------------------------------------