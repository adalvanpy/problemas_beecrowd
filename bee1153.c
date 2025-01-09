#include <stdio.h>
 
int main() {
 
    int n;
    scanf("%d",&n);
    int fat = n;

    for(int i = 1; i < n; i++){
      fat *= i;
    }

    printf("%d\n",fat);
 
    return 0;
}