"""
Exercício Python 11: Faça um programa que leia a largura e a altura de uma parede em metros,
calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro
de tinta pinta uma área de 2 metros quadrados
"""
print("-" * 50)
print(f'{"Calcula total de tinta":^50}')
print("-" * 50)

lagura = float(input("Digite a altura da parede: "))
altura = float(input("Digite a lagura da parede: "))

area = altura * lagura
total_tinta = area * 2

print(f"Área total é {area} metros.\nSerá preciso {total_tinta} litros de tinta.")
