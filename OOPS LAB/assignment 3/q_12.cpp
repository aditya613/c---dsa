#include<iostream>
using namespace std;

void swapValue(int a,int b){
    int temp=a;
    a=b;
    b=temp;
}

void swapReference(int& a,int& b){
    int temp=a;
    a=b;
    b=temp;
}

void swapPointer(int* a,int* b){
    int temp=*a;
    *a=*b;
    *b=temp;
}

int main(){
    int a=10,b=20;

    cout<<"Before pass-by-value: "<<a<<" "<<b<<endl;
    swapValue(a,b);
    cout<<"After pass-by-value: "<<a<<" "<<b<<endl;

    a=10;
    b=20;
    cout<<"Before pass-by-reference: "<<a<<" "<<b<<endl;
    swapReference(a,b);
    cout<<"After pass-by-reference: "<<a<<" "<<b<<endl;

    a=10;
    b=20;
    cout<<"Before pointers: "<<a<<" "<<b<<endl;
    swapPointer(&a,&b);
    cout<<"After pointers: "<<a<<" "<<b<<endl;

    return 0;
}