#include<iostream>
using namespace std;

void modifyPointer(int* p){
    *p=*p+10;
}

void modifyReference(int& x){
    x=x+20;
}

int main(){
    int num=10;
    cout<<"Before: "<<num<<endl;
    modifyPointer(&num);
    cout<<"After pointer function: "<<num<<endl;
    modifyReference(num);
    cout<<"After reference function: "<<num;
    return 0;
}