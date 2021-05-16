"""
Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
"""
print('-' * 30)
print(f'{"Aprovando Emprestímo":^30}')
print('-' * 30)

# solicita o valor do imóvel e salário
valor_imovel = float(input('Digite o valor do imóvel R$ '))
salario = float(input('Digite o valor do seu salário atual R$ '))
parcelamento = int(input('Deseja pagar o imóvel em quanto anos: '))

valor_parcela = valor_imovel / (parcelamento * 12)
condicao = 0.30

if valor_parcela > (salario * condicao):
    print(f'''Emprestímo Negago!\nO Valor das parcelas execedem 30% do seu salário. 
        ''')
else:
    print(f'''
    Emprestímo autorizazdo!
    Valor do imóvel R$ {valor_imovel:.2f}
    Prazo de pagamento {parcelamento * 12} meses
    Valor da parcelas R$ {valor_parcela:.2f}
        ''')
