#include<iostream>
using namespace std;

int divide(int a,int b,int& remainder){
    remainder=a%b;
    return a/b;
}

int main(){
    int a,b,remainder;
    cout<<"Enter two integers: ";
    cin>>a>>b;
    int quotient=divide(a,b,remainder);
    cout<<"Quotient: "<<quotient<<endl;
    cout<<"Remainder: "<<remainder;
    return 0;
}