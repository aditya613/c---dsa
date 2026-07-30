#include<bits/stdc++.h>
using namespace std;


float product(float num1, float num2){
    return num1*num2;
}
float difference(float num1, float num2){
    return num1-num2;
}
float sum(float num1, float num2){
    return num1+num2;
}
int remaind(float num1, float num2){
    return (int)num1 % (int)num2;
}
float quotient(float num1, float num2){
    if(num2==0){
        return 0;
    }
    else{
    return num1/num2;
}
}

int main(){
    float num1,num2;
    cout<<"Enter First Number: ";
    cin>>num1;
    
    cout<<endl<<"Enter Second Number: ";
    cin>>num2;

    cout<<"Sum of Numbers is "<<sum(num1,num2)<<endl;
    
    cout<<"Difference of Numbers is "<<difference(num1,num2)<<endl;
    
    cout<<"Product of Numbers is "<<product(num1,num2)<<endl;
    
    cout<<"Remainder of Numbers is "<<remaind(num1,num2)<<endl;
    
    cout<<"Quotient of Numbers is "<<quotient(num1,num2)<<endl;








}