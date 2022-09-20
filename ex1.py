


# Exercício 02
"""
leia um numero fornecido pelo usuario. Se esse numero por positivo, calcule a raiz quadrada do numero. Se o numero
for negativo informe que o numero é invalido.
"""
num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo numero: '))

if num1> num2:
    print (f' {num1} é maior que {num2}')

elif num1==num2:
    print ('Os numeros sao iguais')

else:
    print(f'{num1} é menor que {num2}')


