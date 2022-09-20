# Exercício 02
"""
leia um numero fornecido pelo usuario. Se esse numero por positivo, calcule a raiz quadrada do numero. Se o numero
for negativo informe que o numero é invalido.
"""
num1 = int(input('Digite um numero: '))

if num1 > 0:
    print(math.sqrt(num1))
elif num1 <= 0:
    print("numero invalido!")

