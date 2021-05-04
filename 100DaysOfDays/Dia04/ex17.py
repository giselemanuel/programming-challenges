"""
Exercício Python 17: Faça um programa que leia o comprimento do cateto oposto e do cateto
adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
"""
import math

print('-' * 40)
print(f'{"Calcula Hipotenusa":^40}')
print('-' * 40)

cateto_oposto = float(input("Insira o valor do cateto oposto: "))
cateto_adjacente = float(input("Insira o valor do cateto adjacente: "))

hipotenusa = math.hypot(cateto_adjacente, cateto_oposto)

print(f"A hipotenusa é {hipotenusa:.2f}.")