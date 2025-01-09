#include <iostream>
using namespace std;
int main(){
    int n; int x = 1;
    cin >> n;
    for(int i = 1; i < n+1; i++){
        cout << i << " " << i*x << " " << i*x*x << endl;
         cout << i << " " << i*x+1 << " " << i*x*x+1 << endl;
        x++;
    }
    return 0;
}