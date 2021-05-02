"""
Exercício Python 12: Faça um algoritmo que leia o preço de um produto e
mostre seu novo preço, com 5% de desconto.
"""
print("-" * 50)
print(f'{"Calcula Desconto":^50}')
print("-" * 50)

valor = float(input("Insira o valor do produto R$ "))
valor_desconto = valor - (valor * 0.05)

print(f"Valor inserido R$ {valor}\nValor com 5% desconto R$ {valor_desconto}")