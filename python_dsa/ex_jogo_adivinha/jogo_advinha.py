# Jogo da Adivinhação

import random

numero_secreto = random.randint(1,20)
tentativa = 1

print("=== JOGO DA ADIVINHAÇÃO ===")
print("Tente adivinhar o número secreto entre 1 e 20")
print(f'Você tem 5 tentativas')

for tentativas in range(1,6):
    print(f'Tentativa {tentativa} de 5')

    try:
        palpite = int(input("Digite seu palpite (1-20): "))
    except ValueError:
        print("Por favor, digite um número válido!")
        continue
        
    if palpite < 1 or palpite > 20:
        print("Por favor, digite um número entre 1 e 20!")
        continue
        
    if palpite == numero_secreto:
        print(f"\n🎉 PARABÉNS! Você acertou! O número era {numero_secreto}.")
        print(f"Você conseguiu em {tentativa} tentativa(s)!")
        break
        
    elif palpite < numero_secreto and palpite > (numero_secreto - 3):
        print("Está Próximo! Tente um número maior.\n")
        tentativa += 1
    elif palpite > numero_secreto and palpite < (numero_secreto + 3):
        print("Está Próximo! Tente um número menor.\n")
        tentativa += 1
    elif palpite < (palpite - numero_secreto):
        print("Está BAIXO! Tente um número maior.\n")
        tentativa += 1
    else:
        print("Está ALTO! Tente um número menor.\n")
        tentativa += 1

        # Última tentativa
    if tentativa == 5:
        print("Última tentativa! Pense bem!")
    
else:
    print(f"\nFIM DE JOGO! Suas tentativas acabaram.")
    print(f"O número secreto era {numero_secreto}.")