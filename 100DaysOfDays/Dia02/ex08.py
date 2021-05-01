"""
Exercício Python 8:
Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
"""

print("-" * 40)
print(f'{"Converte metros em centimetros":^40}')
print("-" * 40)
metro = float(input("Digite o valor em metros: "))
centimetros = metro * 100

print(f"{metro:.0f} metr(s) é equivalente a {centimetros:.0f} centimetro(s).")