#include <stdio.h>
 
int main() {
 
    int m, n, soma;
    while(1 == 1){
        soma = 0;
        scanf("%d%d", &m,&n);
        if( m <= 0 || n <= 0){
            break;
        }
        if(m < n){
            for(; m <= n; m++){
                printf("%d ", m);
                soma = soma + m;
            }
        }
        else{
            for(; n <= m; n++){
                printf("%d ", n);
                soma = soma + n;
            }
        }
        printf("SUM=%d \n", soma);
    }
 
    return 0;
}