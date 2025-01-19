#include <stdio.h>
 
int main() {
 
   int n_teste, numero;
   scanf("%d",&n_teste);
   for(int i = 0; i < n_teste; i++){
    scanf("%d",&numero);
    int soma = 0;
    for(int j = 1; j < numero; j++){
        if (numero % j == 0){
            soma += j;

        }
    }
    if(soma == numero){
        printf("%d eh perfeito\n",numero);
    }
    else{
        printf("%d nao eh perfeito\n",numero);
    }
   }
    return 0;
}