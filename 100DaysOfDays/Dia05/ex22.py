"""
Nessa aula, vamos aprender operações com String no Python.
As principais operações que vamos aprender são o Fatiamento de String,
Análise com len(), count(), find(), transformações com replace(),
upper(), lower(), capitalize(), title(), strip(), junção com join().
"""

print('-' * 40)
print(f'{"Fatiamento de String":^40}')
print('-' * 40)

# definição das variavéis
nome = "gisele"
letra = "e"
frase = "Olá Mundo Mavilhoso"
substitui = frase.replace("Olá", "Tchau")

# exibe string
print(frase)
print(substitui)
print(frase.split())
print("UPPER", nome.upper())
print("LEN", len(nome))
print("LOWER", nome.lower())
print("Capitalize", nome.capitalize())
print("Title", nome.title())
print("Strip", nome.strip())
