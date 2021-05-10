"""
Exercício Python 32: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
"""

print("-" * 40)
print(f'{"Ano Bissexto":^40}')
print("-" * 40)

ano = int(input("Insira um ano: "))

if ano % 4 == 0 and ano % 100 == 0 or ano % 400 == 0:
    print(f"O ano {ano} é BISSEXTO !!!")
else:
    print(f'Este {ano} não é BISSEXTO !!!')