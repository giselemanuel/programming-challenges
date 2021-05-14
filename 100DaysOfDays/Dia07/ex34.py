"""
Exercício Python 34:
Escreva um programa que pergunte o salário de um funcionário e calcule
o valor do seu aumento. Para salários superiores a R$1250,00, calcule
um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
"""
print('-' * 30)
print(f'{"Aumento Multiplo":^30}')
print('-' * 30)

# solicita o salário do funcionário
salario = float(input('Digite o seu salário R$ '))

# calcula aumento salarial
if salario > 1250:
    novo = salario + (salario * 0.10)
else:
    novo = salario + (salario * 0.15)

aumento = novo - salario

# saída com as informações do reajuste do salário
print('Salário atual R$ {:.2f}'.format(salario))
print('Valor do aumento R$ {:.2f}'. format(aumento))
print('Salário reajustado R$ {:.2f}'.format(novo))
