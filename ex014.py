# Exercício Python 14: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
c = float(input('Digite a temperatura em Celsius: '))
f = 9 * c / 5 + 32 #Em um primeiro momento utilezei os () para colocar a multiplicação em evidencia, mas pela ordem de precedencia 'pra esse exemplo' em especifico não é necessário utilizar ().
print('A temperatura em Celsius informada é o equivalente a: {} em ºFahrenheit'.format(f))