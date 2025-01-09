#include <iostream>
using namespace std;

int main(){

    int x,z;
    int y = 0;
    int c = 0;

    cin >> x;
    cin >> z;

    while(z <= x){
        cin >> z;
    }

    for(int i = x; i < z; i++){
       y = y + i;
       c++;

       if(y > z){
        break;
       }

    }
    cout << c << endl;
}