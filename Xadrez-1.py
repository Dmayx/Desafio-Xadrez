#include <stdio.h>

// Módulo Novato: Movimentos básicos com estruturas de repetição simples

void mover_torre(int x, int y) {
    printf("Movimentos possíveis da Torre a partir da posição (%d, %d):\n", x, y);
    for (int i = 1; i <= 8; i++) {
        if (i != x) printf("(%d, %d)\n", i, y); // Verticais
        if (i != y) printf("(%d, %d)\n", x, i); // Horizontais
    }
}

void mover_bispo(int x, int y) {
    printf("Movimentos possíveis do Bispo a partir da posição (%d, %d):\n", x, y);
    for (int i = 1; i <= 8; i++) {
        if (x + i <= 8 && y + i <= 8) printf("(%d, %d)\n", x + i, y + i);
        if (x - i >= 1 && y - i >= 1) printf("(%d, %d)\n", x - i, y - i);
        if (x + i <= 8 && y - i >= 1) printf("(%d, %d)\n", x + i, y - i);
        if (x - i >= 1 && y + i <= 8) printf("(%d, %d)\n", x - i, y + i);
    }
}

void mover_rainha(int x, int y) {
    printf("Movimentos possíveis da Rainha a partir da posição (%d, %d):\n", x, y);
    mover_torre(x, y);
    mover_bispo(x, y);
}

// Módulo Aventureiro: Movimento do Cavalo com loops aninhados

void mover_cavalo(int x, int y) {
    printf("Movimentos possíveis do Cavalo a partir da posição (%d, %d):\n", x, y);
    int movimentos[8][2] = {
        {2, 1}, {1, 2}, {-1, 2}, {-2, 1},
        {-2, -1}, {-1, -2}, {1, -2}, {2, -1}
    };
    for (int i = 0; i < 8; i++) {
        int nx = x + movimentos[i][0];
        int ny = y + movimentos[i][1];
        if (nx >= 1 && nx <= 8 && ny >= 1 && ny <= 8) {
            printf("(%d, %d)\n", nx, ny);
        }
    }
}

// Módulo Mestre: Recursividade para movimentos avançados

void mover_avancado(int x, int y, int profundidade) {
    if (profundidade == 0) return;
    printf("Movimentos avançados a partir de (%d, %d) com profundidade %d:\n", x, y, profundidade);
    mover_rainha(x, y);
    mover_avancado(x, y, profundidade - 1);
}

int main() {
    int x = 4, y = 4; // Posição inicial

    printf("\n=== Módulo Novato ===\n");
    mover_torre(x, y);
    mover_bispo(x, y);
    mover_rainha(x, y);

    printf("\n=== Módulo Aventureiro ===\n");
    mover_cavalo(x, y);

    printf("\n=== Módulo Mestre ===\n");
    mover_avancado(x, y, 2); // Profundidade de 2

    return 0;
}
