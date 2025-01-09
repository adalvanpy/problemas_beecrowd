#include <iostream>
using namespace std;
int main(){

int a,n, z = 0;
cin >> a; cin >> n;

while(n <= 0){
  cin >> n;
}

for(int i = n-1; i >= 0; i--){
    z = z + (a+i);
}  
cout << z;

  return 0;
}