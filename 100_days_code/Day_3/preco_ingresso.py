print("Bem vindo a loja de ingressos da Montanha Russa!")

altura = int(input("Qual a sua altura em cm? "))
ingresso = 0

if altura >= 120:
    print("Você pode entrar na montanha russa!")
    idade = int(input("Qual a sua idade? "))
    if idade < 12:
        ingresso = 10
        print("O preço do ingresso é R$10.")
    elif idade <= 18:
        ingresso = 15
        print("O preço do ingresso é R$15.")
    else:
        ingresso = 30
        print("O preço do ingresso é R$30.")
    
    foto = input("Você gostaria de uma foto do passeio? Digite 'sim' ou 'não': ").lower()
    if foto == "sim":
        ingresso += 10
        
    print(f"O preço total do seu ingresso é R${ingresso}.")
else:
    print("Desculpe, você não pode andar na montanha russa devido à altura.")