#include <stdio.h>
 
int main() {
 
    float nota,total = 0, media = 0;
    int quant = 0;
    while(1==1){
        scanf("%f",&nota);
        if(nota < 0.0 || nota > 10.0){
            printf("nota invalida\n");
        }
        else{
           total = total + nota;
           quant ++;
        }
        if(quant == 2){
            media = total / quant;
            break;
        }
        
    }
    printf("media = %.2f",media);
 
    return 0;
}