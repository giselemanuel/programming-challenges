"""
Exercício Python 7:
Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
"""
print("-" * 40)
print(f'{"Calcula média":^40}')
print("-" * 40)
nota1 = float(input("Insira a primeira nota: "))
nota2 = float(input("Insira a segunda nota: "))

media = (nota1 + nota2) / 2

print(f"Sua média foi {media:.2f}.")