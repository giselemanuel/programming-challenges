"""
Exercício Python 15: Escreva um programa que pergunte a quantidade de Km
percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
"""

print("-" * 50)
print(f'{"Locadora de veículos":^50}')
print("-" * 50)

km = float(input("Informe o total de KM percorrido: "))
dias = int(input("Informe o total de dias: "))

valor_carro = dias * 60
valor_km = km * 0.15
valor_total = valor_carro + valor_km

print(f"Locação do veículo R$ {valor_carro:.2f}\n"
      f"Total de KM rodado R$ {valor_km:.2f}\n"
      f"Valor total a pagar R$ {valor_total:.2f}")