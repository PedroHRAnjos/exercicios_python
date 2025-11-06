# Pedra, Papel e Tesoura

É um jogo de mão simples e popular, geralmente disputado entre duas pessoas. 
O objetivo é derrotar o oponente escolhendo um de três objetos, cada qual com uma vantagem sobre um objeto e uma desvantagem sobre o outro.As regras de vitória são as seguintes:

- Pedra vence a Tesoura (quebrando-a).
- Tesoura vence o Papel (cortando-o).
- Papel vence a Pedra (cobrindo-a).
- Se ambos os jogadores escolherem o mesmo objeto, a rodada resulta em um empate.

### Estrutura

- Apresentação:
  - Jogo Pedra, Papel e Tesoura
  - Regras: Escolha entre 'pedra', 'papel' ou 'tesoura'

- Coleta de dados:
  - Leia jogada do jogador
  - Leia jogada do Computador

- Escolhas:
  - Escrever 'Jogador escolheu: {Escolha}'
  - Escrever 'Computador escolheu: {Escolha}'

### Lógica para determinar vencedor:

```python
 INICIAR
  
  ENQUANTO verdadeiro FAÇA
    ESCREVA "Escolha: Pedra, Papel, Tesoura, Sair"
    LEIA escolha_jogador
    
    SE escolha_jogador == Sair ENTÃO
      PARAR
    FIM SE
    
    SE escolha_jogador não está na lista
      ESCREVA "Escolha inválida! Tente novamente."
      CONTINUAR
    FIM SE
    
    escolha_computador = Escolha aleatória da lista
    
    ESCREVA "Jogador escolheu: " + escolha_jogador
    ESCREVA "Computador escolheu: " + escolha_computador
    
    SE escolha_jogador == escolha_computador ENTÃO
      ESCREVA "Empate!"
    SENÃO
      SE (escolha_jogador == Pedra E escolha_computador == Tesoura) OU
         (escolha_jogador == Papel E escolha_computador == Pedra) OU
         (escolha_jogador == Tesoura E escolha_computador == Papel) ENTÃO
        ESCREVA "Jogador venceu!"
      SENÃO
        ESCREVA "Computador venceu!"
```