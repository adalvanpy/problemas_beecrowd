#include <stdio.h>
 
int main() {
 
    int x,y;
    scanf("%d%d",&x,&y);
    if(x < y){
        while(x < y){
            x ++;
          if(x % 5 == 2 || x % 5 == 3){
            printf("%d\n",x);
          }
        
        }
    }
    else{
        while(y < x){
            y ++;
          if(y % 5 == 2 || y % 5 == 3){
            printf("%d\n",y);
          }
          
        }
    }
    
 
    return 0;
}