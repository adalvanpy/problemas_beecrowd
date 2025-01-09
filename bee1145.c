#include <stdio.h>
 
int main() {
 
    int x,y,z;
    scanf("%d %d",&x,&y);
    z = x;
    for(int i = 1; i < y+1; i++){
        if(i == x){
            printf("%d",i);
        }
        else{
            printf("%d ",i);

        }
        if(i == x){
            printf("\n");
            x = x + z;
        }
        
    }
 
    return 0;
}