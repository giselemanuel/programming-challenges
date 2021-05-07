"""
Exercício Python 24: Crie um programa que leia o nome de uma cidade diga
se ela começa ou não com o nome “SANTO”.
"""
print('-' * 40)
print(f'{"Tem SANTO no nome":^40}')
print('-' * 40)

nome = str(input("Digite seu nome: "))
print(nome[:5] == "santo")
