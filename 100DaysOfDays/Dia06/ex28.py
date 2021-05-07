"""
Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número inteiro
entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.
"""
from random import randint

print('-' * 60)
print(f'{"Jogo da Adivinhação":^60}')
print('-' * 60)
numero_sorteio = randint(0, 5)
numero = int(input("Estou pensando em um número tente adivinhar.\n"
                   "Insira um número entre 0 a 5: "))

if numero == numero_sorteio:
    print("VOCÊ ACERTOU !!!")
else:
    print("VOCÊ ERROU !!!")
