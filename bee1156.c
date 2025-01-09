#include <stdio.h>
 
int main() {
 
    float a = 1,b = 1,c,n = 1;
    float s = 0; 
    for(int i = 3; i < 40; i++){
        if(i % 2 == 1){
          c = a + b;
          s += n + i / c;
          a = c;
          b = c;
          n = 0;
        }
    }
    printf("%.2f\n",s);
 
    return 0;
}