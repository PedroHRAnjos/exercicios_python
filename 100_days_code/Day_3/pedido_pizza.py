# Apresentação
print("Bem vindo à pizzaria Python!")

# Coletando preferências do cliente
tamanho = input("Qual tamanho da pizza você quer? (P/M/G): ").upper()

# Calculando o preço
preco = 0

if tamanho in ['P', 'M', 'G']:
    if tamanho == "P":
            preco += 35           
    elif tamanho == "M":
            preco += 50
    elif tamanho == "G":
            preco += 70

    # Adicionais       
    borda = input("Você quer borda recheada? (sim/não): ").lower()
    if borda == "sim":
            preco += 7

    queijo = input("Você quer adicionar queijo extra? (sim/não): ").lower()
    if queijo == "sim":
            preco += 5

    # Finalizando o pedido      
    print(f"O preço final da sua pizza é R${preco}.")

else:
    print("Tamanho inválido. Por favor, escolha P, M ou G.")
