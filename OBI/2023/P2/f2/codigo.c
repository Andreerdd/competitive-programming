#include <stdio.h>
#include <stdlib.h> // realloc

typedef struct comp {

    int qntd; // quantidade de caracteres
    char c;   // caracteres

} comp_s;

int main(int argc, char ** argv) {

    int comp; // quantidade de caracteres
    
    comp_s * vetor = NULL;
    int tam = 0;

    int qntdUltLetra = 0;
    char ultLetra = '~';
    char l; // letra de agora
    
    scanf("%i%*c", &comp);

    for (int i = 0; i < comp; i++) {
        scanf("%c", &l);
        if (l == ultLetra) {
            // se for um caractere igual ao ultimo, adiciona mais um na quantidade de caracteres
            qntdUltLetra++;
        } else {
            // se for um caractere diferente do ultimo, salva o ultimo
            if (i != 0) {
                vetor = (comp_s *) realloc(vetor, tam+1);
                vetor[tam].qntd = qntdUltLetra;
                vetor[tam].c = ultLetra;
                tam++;    
            }

            ultLetra = l;
            qntdUltLetra = 1;
        }
    }

    // salva o ultimo
    if (ultLetra != '~') {
        vetor = (comp_s *) realloc(vetor, tam+1);
        vetor[tam].qntd = qntdUltLetra;
        vetor[tam].c = ultLetra;
        tam++;    
    }

    printf("\n");

    // printa o que foi comprimido
    for (int j = 0; j < tam; j++) {
        if (j != 0) printf(" ");
        printf("%i %c", vetor[j].qntd, vetor[j].c);
    }

    return 0;
}