"""
Exercício Python 25: Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.
"""

print('-' * 40)
print(f'{"Tem SILVA no nome":^40}')
print('-' * 40)

nome = str(input("Digite seu nome completo: "))
nome = nome.split()

if nome == "silva" or nome == "Silva":
    print(f"Este nome tem SILVA")
else:
    print(f"Este nome não tem SILVA")