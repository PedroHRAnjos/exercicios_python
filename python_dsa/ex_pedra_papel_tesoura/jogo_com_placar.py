def jogo_com_placar():
    """
    Versão alternativa com placar
    """
    opcoes = ["Pedra", "Papel", "Tesoura"]
    vitorias_jogador = 0
    vitorias_computador = 0
    empates = 0
    
    print("=== PEDRA, PAPEL E TESOURA - COM PLACAR ===")
    
    while True:
        print(f"\nPlacar: Jogador {vitorias_jogador} x {vitorias_computador} Computador | Empates: {empates}")
        print("Escolha: 1-Pedra, 2-Papel, 3-Tesoura, 0-Sair")
        
        try:
            escolha_jogador = int(input("Sua escolha: "))
        except ValueError:
            print("Por favor, digite um número válido!")
            continue
        
        if escolha_jogador == 0:
            print(f"\nPlacar Final:")
            print(f"Jogador: {vitorias_jogador}")
            print(f"Computador: {vitorias_computador}")
            print(f"Empates: {empates}")
            break
        
        if escolha_jogador < 1 or escolha_jogador > 3:
            print("Escolha inválida! Digite 1, 2, 3 ou 0 para sair.")
            continue
        
        escolha_computador = random.randint(1, 3)
        
        print(f"\nJogador: {opcoes[escolha_jogador - 1]}")
        print(f"Computador: {opcoes[escolha_computador - 1]}")
        
        if escolha_jogador == escolha_computador:
            print(">>> Empate!")
            empates += 1
        else:
            if (escolha_jogador == 1 and escolha_computador == 3) or \
               (escolha_jogador == 2 and escolha_computador == 1) or \
               (escolha_jogador == 3 and escolha_computador == 2):
                print(">>> Jogador venceu! 🎉")
                vitorias_jogador += 1
            else:
                print(">>> Computador venceu! 💻")
                vitorias_computador += 1

# Menu principal
if __name__ == "__main__":
    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1 - Jogo Simples")
        print("2 - Jogo com Placar")
        print("3 - Sair")
        
        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Opção inválida!")
            continue
        
        if opcao == 1:
            jogo_pedra_papel_tesoura()
        elif opcao == 2:
            jogo_com_placar()
        elif opcao == 3:
            print("Até mais!")
            break
        else:
            print("Opção inválida! Escolha 1, 2 ou 3.")