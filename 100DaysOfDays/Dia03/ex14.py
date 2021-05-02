"""
Exercício Python 14: Escreva um programa que converta uma temperatura digitando
em graus Celsius e converta para graus Fahrenheit.
"""

print("-" * 50)
print(f'{"Conversor de temperatura":^50}')
print("-" * 50)

temperatura_c = float(input("Insira a temperatura em ºC : "))
temperatura_f = (temperatura_c * (9/5)) + 32
print(f"Temperaturas:\n{temperatura_c}ºC\n{temperatura_f}ºF")

