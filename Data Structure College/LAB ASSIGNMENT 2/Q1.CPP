#include<bits/stdc++.h>
using namespace std;


//as it is given n<=12
int factorial(int n){

    if(n==0){
        return 1;
    }

    return n * factorial(n-1);
}


int main(){
    int x;
    cin>>x;

    cout<<"Factorial Of "<<x<<" is : "<<factorial(x);
}