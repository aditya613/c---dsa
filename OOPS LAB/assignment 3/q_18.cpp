#include<iostream>
using namespace std;

float bill(int units,float fixedCharge=100,float rate=5){
    return fixedCharge+(units*rate);
}

int main(){
    int units,choice;
    float fixedCharge,rate;
    cout<<"Enter units: ";
    cin>>units;
    cout<<"Enter 1 for default values or 2 for user-specified values: ";
    cin>>choice;
    if(choice==1){
        cout<<"Electricity bill: "<<bill(units);
    }
    else{
        cout<<"Enter fixed charge: ";
        cin>>fixedCharge;
        cout<<"Enter per-unit rate: ";
        cin>>rate;
        cout<<"Electricity bill: "<<bill(units,fixedCharge,rate);
    }
    return 0;
}