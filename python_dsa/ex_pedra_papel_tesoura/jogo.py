import random

    #   Jogo Pedra, Papel e Tesoura

opcoes = ["Pedra", "Papel", "Tesoura"]
    
print("PEDRA, PAPEL E TESOURA")
print("Bem-vindo ao jogo!")
    
while True:
    print("\n" + "-"*40)
    print("Digite a sua escolha: Pedra, Papel, Tesoura, Sair")
        
    escolha_jogador = input("Sua escolha: ")
        
    # Verificar se o jogador quer sair
    if escolha_jogador == "Sair":
        print("Obrigado por jogar! Até mais!")
        break
        
    # Validar escolha do jogador
    if escolha_jogador not in opcoes:
        print("Escolha inválida! Digite Pedra, Papel, Tesoura ou Sair para sair.")
        continue
        
    # Escolha do computador
    escolha_computador = random.choice(opcoes)
        
    # Ajustar índices para exibição (subtrair 1 para acessar a lista)
    print(f"\nJogador escolheu: {escolha_jogador}")
    print(f"Computador escolheu: {escolha_computador}")
        
    # Determinar o vencedor
    if escolha_jogador == escolha_computador:
        print(">>> Empate!")
    else:
        # Verificar condições de vitória do jogador
        if (escolha_jogador == "Pedra" and escolha_computador == "Tesoura") or \
            (escolha_jogador == "Papel" and escolha_computador == "Pedra") or \
            (escolha_jogador == "Tesoura" and escolha_computador == "Papel"):
            print(">>> Você venceu! 🎉")
        else:
            print(">>> Computador venceu! 💻")