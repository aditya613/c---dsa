#include<bits/stdc++.h>
using namespace std;

void swapByValue(int a, int b){
    int temp = a;
    a = b;
    b = temp;

    cout<<"a is "<<a<<endl;
    cout<<"b is "<<b<<endl;

}

void swapByReference(int &a, int &b){

    int temp = a;
    a = b;
    b = temp;


    
    cout<<"a is "<<a<<endl;
    cout<<"b is "<<b<<endl;
    
}

int main(){

    int a, b;
    cin>>a;
    cout<<endl;
    cin>>b;

    swapByValue(a,b);

    swapByReference(a,b);


    return 0;
}