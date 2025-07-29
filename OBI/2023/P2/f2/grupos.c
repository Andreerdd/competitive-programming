#include <stdio.h>
#include <stdlib.h>

typedef struct par_s {
    int a;
    int b;
} par_t;

int main(int argc, char ** argv) {

    int E, G, N; // Estudantes Totais, Gostariam, Nao gostariam

    par_t * gostariam;
    int qntdGostariam = 0;

    par_t * nao_gostariam;
    int qntdNaoGostariam = 0;

    int x, y, z, temp;
    int restricoes_quebradas = 0;

    // Pede os valores
    scanf("%i %i %i", &E, &G, &N);

    gostariam     = (par_t *)malloc(sizeof(par_t) * G);
    nao_gostariam = (par_t *)malloc(sizeof(par_t) * N);

    // Pede os pares que gostariam
    for (int i = 0; i < G; i++) {
        scanf("%i %i", &(gostariam[i].a), &(gostariam[i].b));
        qntdGostariam++;
    }

    // Pede os pares que nao gostariam
    for (int i = 0; i < N; i++) {
        scanf("%i %i", &(nao_gostariam[i].a), &(nao_gostariam[i].b));
        qntdNaoGostariam++;
    }

    // Pede os grupos
    for (int i = 0; i < E/3; i++) {
        scanf("%i %i %i", &x, &y, &z);

        temp = 0;

        // Verifica se x, y e z está com quem gostaria
        for (int j = 0; j < qntdGostariam; j++) {
            if (gostariam[j].a == x) {
                if (!(gostariam[j].b == y || gostariam[j].b == z)) { // se os outros nao for com quem x gostar
                    temp++;
                     
                }
            }
        
            if (gostariam[j].a == y) {
                if (!(gostariam[j].b == x || gostariam[j].b == z)) { // se os outros nao for com quem x gostar
                    temp++;
                     
                }
            }
        
            if (gostariam[j].a == z) {
                if (!(gostariam[j].b == x || gostariam[j].b == y)) { // se os outros nao for com quem x gostar
                    temp++;
                     
                }
            }
        }

        // Verifica se x, y e z não está com quem não gostaria
        for (int j = 0; j < qntdNaoGostariam; j++) {
            if (nao_gostariam[j].a == x) {
                if ((nao_gostariam[j].b == y || nao_gostariam[j].b == z)) { // se os outros nao for com quem x gostar
                    temp++;
                     
                }
            } 
            if (nao_gostariam[j].a == y) {
                if ((nao_gostariam[j].b == x || nao_gostariam[j].b == z)) { // se os outros nao for com quem x gostar
                    temp++;
                     
                }
            }
            if (nao_gostariam[j].a == z) {
                if ((nao_gostariam[j].b == x || nao_gostariam[j].b == y)) { // se os outros nao for com quem x gostar
                    temp++;
                     
                }
            }
        }

        restricoes_quebradas += temp;

    }

    // printa a restrição
    printf("%i", restricoes_quebradas);

    return 0;
}   