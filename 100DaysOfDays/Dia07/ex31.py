"""
Exercício Python 31: Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta
viagens mais longas.
"""

print("-" * 40)
print(f'{"Custo da viagem":^40}')
print("-" * 40)

curta = 0
longa = 0
km = float(input("Insira a distância em km da viagem : "))

if km <= 200:
    curta = km * 0.50
    print(f"Valor total de {km} é de R$ {curta:.2f}.")
else:
    longa = km * 0.45
    print(f"Valor total de {km} km é de R$ {longa:.2f}.")

