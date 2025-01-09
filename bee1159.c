#include <stdio.h>
 
int main() {
 
   int soma = 0, x, cont = 0;

   while(1 == 1){

      scanf("%d",&x);
      if(x == 0){
        break;
      }

      while(1==1){

         if(x % 2 == 0){
            soma = soma + x;
            cont++;
         }
         x++;

         if(cont == 5){
            break;
         }
         
      }
      printf("%d\n",soma);
      soma = 0;
      cont = 0;
   }
 
    return 0;
}