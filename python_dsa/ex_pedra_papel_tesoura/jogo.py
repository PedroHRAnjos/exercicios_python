import random

def jogo_pedra_papel_tesoura():
    """
    Implementação do jogo Pedra, Papel e Tesoura
    """
    opcoes = ["Pedra", "Papel", "Tesoura"]
    
    print("=== PEDRA, PAPEL E TESOURA ===")
    print("Bem-vindo ao jogo!")
    
    while True:
        print("\n" + "="*40)
        print("Escolha: 1-Pedra, 2-Papel, 3-Tesoura, 0-Sair")
        
        try:
            escolha_jogador = int(input("Sua escolha: "))
        except ValueError:
            print("Por favor, digite um número válido!")
            continue
        
        # Verificar se o jogador quer sair
        if escolha_jogador == 0:
            print("Obrigado por jogar! Até mais!")
            break
        
        # Validar escolha do jogador
        if escolha_jogador < 1 or escolha_jogador > 3:
            print("Escolha inválida! Digite 1, 2, 3 ou 0 para sair.")
            continue
        
        # Escolha do computador
        escolha_computador = random.randint(1, 3)
        
        # Ajustar índices para exibição (subtrair 1 para acessar a lista)
        print(f"\nJogador escolheu: {opcoes[escolha_jogador - 1]}")
        print(f"Computador escolheu: {opcoes[escolha_computador - 1]}")
        
        # Determinar o vencedor
        if escolha_jogador == escolha_computador:
            print(">>> Empate!")
        else:
            # Verificar condições de vitória do jogador
            if (escolha_jogador == 1 and escolha_computador == 3) or \
               (escolha_jogador == 2 and escolha_computador == 1) or \
               (escolha_jogador == 3 and escolha_computador == 2):
                print(">>> Jogador venceu! 🎉")
            else:
                print(">>> Computador venceu! 💻")