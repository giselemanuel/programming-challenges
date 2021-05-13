"""
Exercício Python 33:
Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
"""
print('-' * 30)
print(f'{"Valores - Maior e Menor":^30}')
print('-' * 30)

num1 = int(input('Digite o 1º número: '))
num2 = int(input('Digite o 2º número: '))
num3 = int(input('Digite o 3º número: '))

maior = num1
menor = num1

# verificar quem é o maior
if num2 > num1 and num2 > num3:
    maior = num2
if num3 > num1 and num3 > num2:
    maior = num3

# verificar quem é o menor
if num2 < num1 and num2 < num3:
    menor = num2
if num3 < num1 and num3 < num2:
    menor = num3

print(f'Maior número é : {maior}')
print(f'Menor é número : {menor}')