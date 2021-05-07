"""
Exercício Python 27: Faça um programa que leia o nome completo de uma pessoa,
mostrando em seguida o primeiro e o último nome separadamente.
"""
print('-' * 60)
print(f'{"Primeiro e último nome de uma pessoa":^60}')
print('-' * 60)

nome = str(input("Digite seu nome completo: "))
nome = nome.split()
ultimo = len(nome) - 1

print(f"Seu primeiro nome é: {nome[0]}")
print(f"Seu último nome é: {nome[ultimo]}")