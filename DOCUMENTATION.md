
# 📘 DOCUMENTAÇÃO DO PROJETO: Simulador de Movimentos de Xadrez com Estruturas de Repetição em C

---

#### 🗂️ Visão Geral

Este projeto tem como objetivo aplicar conceitos fundamentais de programação em C, utilizando estruturas de repetição e recursividade para simular os movimentos das peças de xadrez em um tabuleiro 8x8. O projeto é dividido em três módulos com níveis de dificuldade crescente.

---

#### 🛠️ Requisitos

- Compilador C (GCC ou similar)
- Conhecimentos básicos de lógica de programação
- Editor de texto ou IDE para escrever e compilar o código

---

#### 📂 Estrutura do Projeto

O código está organizado em funções específicas para cada peça de xadrez:

- `mover_torre(int x, int y)`
- `mover_bispo(int x, int y)`
- `mover_rainha(int x, int y)`
- `mover_cavalo(int x, int y)`
- `mover_avancado(int x, int y, int profundidade)`

---

#### 🔍 Explicação das Funções

- **`mover_torre(int x, int y)`**  
  Simula os movimentos verticais e horizontais da Torre.

- **`mover_bispo(int x, int y)`**  
  Simula os movimentos diagonais do Bispo.

- **`mover_rainha(int x, int y)`**  
  Combina os movimentos da Torre e do Bispo.

- **`mover_cavalo(int x, int y)`**  
  Usa loops aninhados para simular o movimento em "L" do Cavalo.

- **`mover_avancado(int x, int y, int profundidade)`**  
  Utiliza recursividade para simular movimentos avançados com profundidade.

---

#### ⚙️ Instruções de Compilação e Execução

1. Compile o código com um compilador C:
