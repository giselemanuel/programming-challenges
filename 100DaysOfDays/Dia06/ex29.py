"""
Exercício Python 29: Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite.
"""
print("-" * 40)
print(f"{'Radar Eletrônico':^40}")
print("-" * 40)

multa = 7
km = float(input("Insira a sua velocidade (km) : "))

if km > 80:
    multa = multa * (km - 80)
    print(f"Sua multa é de R$ {multa:.2f}")
else:
    print("Obrigada por dirigir no limite da velocidade.")