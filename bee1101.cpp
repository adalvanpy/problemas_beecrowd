#include <iostream>
using namespace std;
int main(){
    int m, n, soma;
    while(true){
        soma = 0;
        cin >> m;
        cin >> n;

        if(m <= 0 || n <= 0){
            break;
        }

        if(m < n){
          while(m <= n){
            cout << m << " ";
            soma = soma + m;
            m++;
          }
        }

        else{
          while(n <= m){
            cout << n << " ";
            soma = soma + n;
            n++;
          }
        }

        cout << "Sum=" << soma;
    }
    return 0;
}