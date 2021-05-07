"""
Exercício Python 26: Faça um programa que leia uma frase pelo teclado e
mostre quantas vezes aparece a letra “A”, em que posição ela aparece a
primeira vez e em que posição ela aparece a última vez.
"""
print('-' * 60)
print(f'{"Primeira e última ocorrência em uma Strig":^60}')
print('-' * 60)

frase = str(input("Digite uma frase: ")).upper()
print(f"Total de Letras A", frase.count("A"))
print(f"A primeira letra A esta na posição: {frase.find('A') + 1}")
print(f"A última letra A esta na posição:{frase.rfind('A') + 1}")