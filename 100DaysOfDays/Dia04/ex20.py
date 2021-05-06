"""
Exercício Python 20: O mesmo professor do desafio 19 quer sortear a ordem de apresentação de
trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
"""

from random import shuffle

print('-' * 40)
print(f'{"Sorteia ordem de apresentação":^40}')
print('-' * 40)

turma = []

for a in range(1, 5):
    nome = str(input("Digite o nome de um aluno: "))
    turma.append(nome)
shuffle(turma)
print(f"--\nOrdem de apresentação é: {turma}")