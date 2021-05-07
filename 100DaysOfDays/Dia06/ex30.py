"""
Exercício Python 30: Crie um programa que leia um número inteiro e
mostre na tela se ele é PAR ou ÍMPAR.
"""
print("-" * 40)
print(f'{"PAR ou IMPAR?":^40}')
print("-" * 40)

num = int(input("Digite um número: "))
if num % 2 == 0:
    print(f"{num} é PAR.")
else:
    print(f"{num} é IMPAR.")