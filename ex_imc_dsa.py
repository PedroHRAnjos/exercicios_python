##Exercício 30
##Escreva um programa que peça ao usuário para digitar sua altura em metros (ex: 1.75) e seu peso em quilogramas (ex: 68.5). Calcule o Índice de Massa Corporal (IMC) usando a fórmula IMC = peso / (altura * altura) e imprima o resultado formatado com duas casas decimais.


# Solução
altura = float(input("Digite sua altura em metros:"))
peso = float(input("Digite seu peso em kgs:"))
imc = peso / (altura * altura)
if imc < 18.5:
    print(f"Seu imc é: {imc:.2f} - Magreza")
elif imc >= 18.5 and imc <= 24.9:
    print(f"Seu imc é: {imc:.2f} - Peso normal")
elif imc >= 25.0 and imc <= 29.9:
    print(f"Seu imc é: {imc:.2f} - Sobrepeso")
elif imc >= 30.0 and imc <= 34.9:
    print(f"Seu imc é: {imc:.2f} - Obesidade grau I")
elif imc >= 35.0 and imc <= 39.9:
    print(f"Seu imc é: {imc:.2f} - Obesidade grau II (Severa)")
else: # A última condição (acima de 40) não precisa de elif
    print(f"Seu imc é: {imc:.2f} - Obesidade grau III (Mórbida)")