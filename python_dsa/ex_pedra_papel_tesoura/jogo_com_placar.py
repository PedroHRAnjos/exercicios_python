# Versão alternativa com placar

import random
    
opcoes = ["Pedra", "Papel", "Tesoura"]
vitorias_jogador = 0
vitorias_computador = 0
empates = 0

print("=== PEDRA, PAPEL E TESOURA - COM PLACAR ===")

while True:
    print(f"\nPlacar: Jogador {vitorias_jogador} x {vitorias_computador} Computador | Empates: {empates}")
    print("Digite a sua escolha: Pedra, Papel, Tesoura ou Sair")
    
    escolha_jogador = input("Sua escolha: ")
    
    if escolha_jogador == "Sair":
        print(f"\nPlacar Final:")
        print(f"Jogador: {vitorias_jogador}")
        print(f"Computador: {vitorias_computador}")
        print(f"Empates: {empates}")
        break
    
    if escolha_jogador not in opcoes:
        print("Escolha inválida! Digite Pedra, Papel, Tesoura ou Sair para sair.")
        continue
    
    escolha_computador = random.choice(opcoes)
    
    print(f"\nJogador: {escolha_jogador}")
    print(f"Computador: {escolha_computador}")
    
    if escolha_jogador == escolha_computador:
        print(">>> Empate!")
        empates += 1
    else:
        if (escolha_jogador == "Pedra" and escolha_computador == "Tesoura") or \
            (escolha_jogador == "Papel" and escolha_computador == "Pedra") or \
            (escolha_jogador == "Tesoura" and escolha_computador == 'Papel'):
            print(">>> Jogador venceu! 🎉")
            vitorias_jogador += 1
        else:
            print(">>> Computador venceu! 💻")
            vitorias_computador += 1