"""
Exercício Python 18: Faça um programa que leia um ângulo qualquer
e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
"""
import math

print('-' * 40)
print(f'{"Exibe, Seno,Cosseno e Tangente":^40}')
print('-' * 40)

angulo = float(input("Digite um angulo: "))
cosseno = math.cos(angulo)
tangente = math.tan(angulo)
seno = math.sin(angulo)

print(f"Angulo inserido foi {angulo}º\n"
      f"Seno é {seno:.2f}.\n"
      f"Cosseno é {cosseno:.2f}.\n"
      f"Tangente é {tangente:.2f}.")
