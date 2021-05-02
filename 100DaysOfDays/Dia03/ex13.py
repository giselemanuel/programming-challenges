"""
Exercício Python 13: Faça um algoritmo que leia o salário de um funcionário
e mostre seu novo salário, com 15% de aumento.
"""

print("-" * 50)
print(f'{"Reajusta salário":^50}')
print("-" * 50)

salario = float(input("Insira o seu salário R$ "))
novo_salario = salario + (salario * 0.15)
print(f"Seu salário atual R$ {salario:.2f}\nSalario com aumento de 15% R$ {novo_salario:.2f}")