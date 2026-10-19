#include <iostream>
#include "MathUtils.h"
using namespace std ;

int main(){
    test t1 ;
    bool ans = t1.isPrime(5);
    if(ans == true ){
        cout << "true" << endl;
    }else{
        cout << "false" << endl;
    }
    int a = t1.fact(5);
    cout << a << endl;

    int b = t1.GCD(4 ,5);
    cout << b << endl;

    int c = t1.power(3 ,2);
    cout << c << endl;
    return 0;
}