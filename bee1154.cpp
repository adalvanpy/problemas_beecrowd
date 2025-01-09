#include <stdio.h>

int main (){

    int idade, idades = 0;
     
    float media,quant = 0;;

    while(1==1){
        scanf("%d",&idade);

        if(idade < 0){
            break;
        }

        else{
            idades = idades + idade;
            quant ++;
        }

    }
    media = idades / quant;
    printf("%.2f\n",media);
}