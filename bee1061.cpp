#include <iostream>
#include <string>
using namespace std;

int main(){
string lixo;
int dia1, hora1, minuto1, segundo1;
int dia2, hora2, minuto2, segundo2;

cin >> lixo >> dia1;
cin >> hora1 >> lixo >> minuto1 >> lixo >> segundo1;

cin >> lixo >> dia2;
cin >> hora2 >> lixo >> minuto2 >> lixo >> segundo2;

int inicio = dia1 * 86400 + hora1 * 3600 + minuto1 * 60 + segundo1;
int fim = dia2 * 86400 + hora2 * 3600 + minuto2 * 60 + segundo2;


int diferenca = (fim - inicio);


int dias = diferenca / 86400 ;

diferenca %= 86400 ;

int horas = diferenca / 3600;

diferenca %= 3600;

int minutos = diferenca / 60;

int segundos = diferenca % 60;


cout << dias << " dia(s)" << endl;
cout << horas << " hora(s)" << endl;
cout << minutos << " minuto(s)" << endl;
cout << segundos << " segundo(s)"<< endl;

return 0;

}