# Calculadora de Gorjetas

# Este programa calcula quanto cada pessoa deve pagar em uma conta de restaurante
print("Bem vindo a calculador de gorjetas!")

# Solicita o valor da conta, a porcentagem de gorjeta e o número de pessoas
conta = float(input("Qual o valor da conta? R$"))
gorjeta = int(input("Qual porcentagem de gorjeta você gostaria de dar? 10, 12 ou 15? "))
pessoas = int(input("Em quantas pessoas a conta será dividida? "))

# Calcula o valor da gorjeta, o total da conta e quanto cada pessoa deve pagar
valor_gorjeta = conta * (gorjeta / 100)
valor_total = conta + valor_gorjeta
valor_por_pessoa = round(valor_total / pessoas, 2)

print(f"Cada pessoa deve pagar: R${valor_por_pessoa:.2f}")