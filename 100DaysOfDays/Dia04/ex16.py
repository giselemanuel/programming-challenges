"""
Exercício Python 16: Crie um programa que leia um número
Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
"""

print('-' * 40)
print(f'{"Exibe um número inteiro":^40}')
print('-' * 40)


numero = float(input("Insira um número real: "))
print(f"O número inteiro de {numero} é {round(numero)}")