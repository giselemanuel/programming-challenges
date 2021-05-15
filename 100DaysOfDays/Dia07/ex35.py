"""
Exercício Python 35: Desenvolva um programa que leia o comprimento de
três retas e diga ao usuário se elas podem ou não formar um triângulo.
Para que seja possível a formação de um triângulo, a medida do
lado  deve ser menor do que a soma das medidas dos outros dois lados.
"""

# cabeçalho do programa
print('-' * 30)
print(f'{"Analisando o Triângulo":^30}')
print('-' * 30)

# entrada dos valores dos lados do triângulo
lado1 = int(input('Digite o valor do lado 1: '))
lado2 = int(input('Digite o valor do lado 2: '))
lado3 = int(input('Digite o valor do lado 3: '))

# encontro o maior valor
if lado1 < (lado2 + lado3) and lado2 < (lado1 + lado3) and lado3 < (lado2 + lado1):
    print('-\nÉ possível criar um triângulo.')
else:
    print('-\nNão é possível criar um triângulo.')