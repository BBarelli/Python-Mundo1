# Exercício Python 26: Faça um programa que leia uma frase pelo teclado e mostre:


# 1.Quantas letras 'a'
frase = str(input('Digite uma frase: ')).upper().strip()
print('Quantas vezes a letra (a) aparece na frase: {}'.format(frase.count('A')))

# 2.Em que posição ela aparece a primeira vez
print('Em que posição ela aparece a primeira vez: {}'.format(frase.find('A')+1))

# 3.Em que posição ela aparece a última vez
# o rfind: Procure a partir do lado direito
print('Em que posição ela aparece a última vez: {}'.format(frase.rfind('A')+1))
