# Aula 10: Condições simples e compostas 
'''Estrutura condicional: o bloco Verdadeiro é execultado ou o False, NUNCA os dois blocos serão execultados

if carro.esquerda():
    bloco True

else: 
    bloco False
'''
tempo = int(input('Quantos anos o seu carro tem? '))
#Se
if tempo <=3:
    print('Seu carro é novo!')
#Se não
else:
    print('Seu carro é velho.')
print('Fim')

#Condição Simplificada
tempo = int(input('Quantos anos tem o seu carro? '))
print('Carro novo' if tempo <=3 else 'Carro velho')
print('Fim')

#Exemplos prático: Estrutura condicional SIMPLES (Sem else)

nome = str(input('Digite seu nome: ')).strip()
#String sempre deve ser entre aspas simples
if nome == 'Breno':
    print('Nossa que nome lindo você tem! rsrs')
print('Olá {}, seja muito bem-vindo(a)'.format(nome))

#Exemplos prático: Estrutura condicional COMPOSTA com if e else
n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
m = (n1+n2)/2
print('Sua média foi {:.1f}'.format(m))
if m >= 6.0:
    print('Parabéns você está acima da média.')
else:
    print('Que pena, você precisa estudar mais.')

# Condição simplificada
print('Parabéns pela sua aprovação!' if m >= 7 else 'Infelizmente você está Reprovado')