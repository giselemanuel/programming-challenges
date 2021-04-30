"""
Dissecando uma variável:
Faça um programa que leia algo pelo teclado e mostre na tela o
seu tipo primitivo e todas as informações possíveis sobre ele.
"""

print("-------- DISSECANDO UMA VARIÁVEL --------")
entrada = input("Digite algo: ")
print("O tipo primitivo deste valor é: ", type(entrada))
print("Só tem espaços.", entrada.isspace())
print("É um número: ", entrada.isnumeric())
print("Esta em minuscúla: ", entrada.islower())
print("Esta em maiuscúla: ", entrada.isupper())
print("Esta capitalizada: ", entrada.title())