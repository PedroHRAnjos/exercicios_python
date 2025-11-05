Pedra, Papel e Tesoura é um jogo de mão simples e popular, geralmente disputado entre duas pessoas. 
O objetivo é derrotar o oponente escolhendo um de três objetos, cada qual com uma vantagem sobre um objeto e uma desvantagem sobre o outro.As regras de vitória são as seguintes:

-Pedra vence a Tesoura (quebrando-a).
-Tesoura vence o Papel (cortando-o).
-Papel vence a Pedra (cobrindo-a).

Se ambos os jogadores escolherem o mesmo objeto, a rodada resulta em um empate.

//Estrutura

- Apresentação:
Jogo Pedra, Papel e Tesoura
Regras: Escolha entre 'pedra', 'papel' ou 'tesoura'

- Coleta de dados:
Leia jogada do jogador 1
Leia jogada do Computador

- Tratamento de dados:
Converter jogada do jogador para letras sem espaços
Converter jogada do computador para palavra sem espaços

Escrever 'Jogador escolheu: {Escolha}'
Escrever 'Computador escolheu: {Escolha}'

Lógica para determinar vencedor:

INICIAR
  OPCOES = ["Pedra", "Papel", "Tesoura"]
  
  ENQUANTO verdadeiro FAÇA
    ESCREVA "Escolha: 1-Pedra, 2-Papel, 3-Tesoura, 0-Sair"
    LEIA escolha_jogador
    
    SE escolha_jogador == 0 ENTÃO
      PARAR
    FIM SE
    
    SE escolha_jogador < 1 OU escolha_jogador > 3 ENTÃO
      ESCREVA "Escolha inválida! Tente novamente."
      CONTINUAR
    FIM SE
    
    escolia_computador = NUMERO_ALEATORIO(1, 3)
    
    ESCREVA "Jogador escolheu: " + OPCOES[escolha_jogador - 1]
    ESCREVA "Computador escolheu: " + OPCOES[escolia_computador - 1]
    
    SE escolha_jogador == escolia_computador ENTÃO
      ESCREVA "Empate!"
    SENÃO
      SE (escolha_jogador == 1 E escolia_computador == 3) OU
         (escolha_jogador == 2 E escolia_computador == 1) OU
         (escolha_jogador == 3 E escolia_computador == 2) ENTÃO
        ESCREVA "Jogador venceu!"
      SENÃO
        ESCREVA "Computador venceu!"
      FIM SE
    FIM SE
  FIM ENQUANTO
FIM