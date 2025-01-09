#include <stdio.h>
 
int main() {
 
    int grenais = 0, inter = 0, gremio = 0, empate = 0;
    int grem, inte;
    while(1==1){
        scanf("%d%d",&inte,&grem);
        if(grem == inte){
            empate ++;
        }
        grenais ++;
        if(inte > grem){
           inter ++;
        }
        else{
            gremio ++;
        }
        printf("Novo grenal (1-sim 2-nao)\n");
        int novo;
        scanf("%d",&novo);
        if(novo == 1){
          continue;
            }
        else if(novo == 2){
            break;
        }
        }
    printf("%d grenais\n",grenais);
    printf("Inter:%d\n",inter);
    printf("Gremio:%d\n",gremio);
    printf("Empates:%d\n",empate);
    if(inter > gremio){
        printf("Inter venceu mais\n");
    }
    else if(gremio > inter){
        printf("Gremio venceu mais\n");
    }
    else if(inter == gremio){
        printf("Nao houve vencedor\n");
    }
        
    return 0;
}