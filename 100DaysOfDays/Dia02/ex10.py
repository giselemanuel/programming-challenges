"""
Exercício Python 10:
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre
quantos dólares ela pode comprar.
"""

print("-" * 50)
print(f'{"Converte Dollar":^50}')
print("-" * 50)

real = float(input("Informe um valor R$ "))
dolar = real / 5.44
print(f"Com o valor R${real} você consegue comprar U${dolar:.0f}.")