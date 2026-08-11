#include<bits/stdc++.h>
using namespace std;

int main(){
    int num1,num2,num3;
    int largest;

    cout<<"Enter First Number: ";
    cin>>num1;

    cout<<endl<<"Enter Second Number: ";
    cin>>num2;

    cout<<endl<<"Enter Third Number: ";
    cin>>num3;

    if(num1>num2){
        if(num1>num3){
            largest = num1;
        }
        else{
            largest=num3;
        }
    }
    else{
        if(num2>num3){
            largest = num2;
        }
        else{
            largest=num3;
        }
    }

    cout<<"Largest Number is "<<largest<<endl;
    cout<< ((largest%2==0)? "It is even number" : "It is odd number");
}