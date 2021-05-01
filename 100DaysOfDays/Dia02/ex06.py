"""
Exercício Python 006:
Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada
"""
print("-" * 60)
print(f'{"Exibe Dobro, Triplo e a Raiz Quadrada ":^60}')
print("-" * 60)
numero = int(input("Insira um número: "))

dobro = numero * 2
triplo = numero * 3
raiz = numero ** 0.5

print(f"O dobro de {numero} é {dobro}.\nO triplo de {numero} é {triplo}.\nA raiz qudrada de {numero} é {raiz:.2f}.")