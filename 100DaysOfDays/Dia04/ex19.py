"""
Exercício Python 19: Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
"""

import random

print('-' * 40)
print(f'{"Sorteia Aluno":^40}')
print('-' * 40)

turma = []

for aluno in range(1, 5):
    nome = str(input("Digite o nome de um aluno: "))
    turma.append(nome)

sorteio = random.choice(turma)

print(f"--\nO(a) aluno(a) escolhido(a) foi {sorteio}")