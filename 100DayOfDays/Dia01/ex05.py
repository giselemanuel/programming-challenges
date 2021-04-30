"""
Antecessor e Sucessor
Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.
"""
print("------ ANTECESSOR E SUCESSOR ------")
numero = int(input("Digite um número: "))
antecessor = numero - 1
sucessor = numero + 1

print(f"Você digitou {numero}.\nO seu antecessor é {antecessor}.\nO seu sucessor é {sucessor}.")