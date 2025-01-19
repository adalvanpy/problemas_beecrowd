#include <iostream>
using namespace std;
int main(){

    int n_testes,numero;
    cin >> n_testes;

    for(int i = 0; i < n_testes; i++ ){
        cin >> numero;
        int vezes = 0;

        for(int j = 1; j <= numero; j++){
            if(numero % j == 0){
                vezes += 1;
            }
            
        }
        if(vezes > 2){
            cout << numero << " nao eh primo" << endl;
        }
        else{
            cout << numero << " eh primo" << endl;
        }
    }

    return 0;
}