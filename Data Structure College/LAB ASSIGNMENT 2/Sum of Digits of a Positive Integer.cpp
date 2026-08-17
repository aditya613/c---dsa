#include<bits/stdc++.h>
using namespace std;

int sum_digits(int n){

    if(n<10){
        return n;
    }

    return (n % 10) + sum_digits(n / 10); 
}

int main(){

    int x;
    cout<<"Enter Number to calculate sum of the digits: ";

    cin>>x;

    cout<<"Ans is "<<sum_digits(x);
}