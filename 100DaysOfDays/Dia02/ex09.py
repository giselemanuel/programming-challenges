"""
Exercício Python 9:
Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.
"""
print("-" * 50)
print(f'{"Tabuada":^50}')
print("-" * 50)

numero = int(input("Digite um número: "))
print("\n------------")
for tabuada in range(1, 11):
    print(f"{tabuada} x {numero} = {tabuada * numero}")
print("------------")