# ♟️ Simulador de Movimentos de Xadrez com Estruturas de Repetição em C

## 🧩 Itens Iniciais

Este projeto tem como objetivo aplicar conceitos fundamentais de programação em C, utilizando estruturas de repetição e recursividade para simular os movimentos das peças de xadrez em um tabuleiro 8x8.

## 🎯 Objetivos

- Aplicar **estruturas de repetição simples** (`for`, `while`, `do-while`) para simular os movimentos básicos da **Torre**, **Bispo** e **Rainha**.
- Utilizar **loops aninhados** para simular o movimento em "L" do **Cavalo**.
- Implementar **recursividade** e **loops complexos** com múltiplas condições para simular movimentos avançados das peças.

## 🚀 Introdução

Seja bem-vindo a uma jornada que transformará seus conhecimentos em habilidades práticas de programação!

Imagine que você foi contratado pela **MateCheck**, uma empresa inovadora que desenvolve jogos para ensinar programação. Seu primeiro grande projeto? Um **jogo de xadrez revolucionário**, onde as peças são controladas por **linhas de código**!

Neste projeto, você não apenas aprenderá a programar, mas também entenderá como aplicar lógica e estruturas de repetição para resolver problemas reais. O projeto é dividido em três módulos com níveis de dificuldade crescente:

### 👨‍💻 Módulo Novato
Você dará os primeiros passos utilizando `for`, `while` e `do-while` para controlar os movimentos lineares da **Torre**, **Bispo** e **Rainha**.

### 🧗 Módulo Aventureiro
O desafio aumenta! Aqui você implementará **loops aninhados** para simular o movimento em "L" do **Cavalo**, exigindo maior atenção à lógica e às condições do tabuleiro.

### 🧙 Módulo Mestre
Você atingirá o auge da sua jornada, dominando a **recursividade** e utilizando **loops complexos** com múltiplas variáveis e condições para refinar seus códigos e simular movimentos avançados.

## 📂 Estrutura do Código

O código está organizado em funções específicas para cada peça:

- `mover_torre(int x, int y)`
- `mover_bispo(int x, int y)`
- `mover_rainha(int x, int y)`
- `mover_cavalo(int x, int y)`
- `mover_avancado(int x, int y, int profundidade)`

Cada função imprime no terminal os movimentos possíveis da peça a partir de uma posição inicial no tabuleiro.

## 🛠️ Como Executar

1. Compile o código com um compilador C, como `gcc`:
   ```bash
   gcc xadrez.c -o xadrez
   ```
