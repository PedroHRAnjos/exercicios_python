# Gerador de senhas

import random

letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
simbolos = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Bem-vindo ao gerador de senhas!")
num_letras = int(input("Quantas letras você quer na sua senha?\n"))
num_simbolos = int(input("Quantos símbolos você quer?\n"))
num_numeros = int(input("Quantos números você quer?\n"))


# Gerador de senha fácil
# senha = ""

# for char in range(1, num_letras + 1):
#     senha += random.choice(letras)

# for char in range(1, num_simbolos + 1):
#     senha += random.choice(simbolos)

# for char in range(1, num_numeros + 1):
#     senha += random.choice(numeros)

# print(senha)

# Gerador de senha difícil
senha_dificil = [] 

for char in range(1, num_letras + 1):
    senha_dificil.append(random.choice(letras))

for char in range(1, num_simbolos + 1):
    senha_dificil.append(random.choice(simbolos))

for char in range(1, num_numeros + 1):
    senha_dificil.append(random.choice(numeros))

random.shuffle(senha_dificil)

senha = ""
for char in senha_dificil:
    senha += char

print(f"Sua senha é: {senha}")