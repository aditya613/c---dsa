#include<bits/stdc++.h>
using namespace std;

int main(){

    int a,b,c;
    cout<<"Enter first number: ";
    cin>>a;
    cout<<"Enter Second number: ";
    cin>>b;
    cout<<"Enter third number: ";
    cin>>c;

    int largest = (a>b)?((a>c)?a:c):((b>c)?b:c);

    cout<<"Largest Number is : "<<largest;

}