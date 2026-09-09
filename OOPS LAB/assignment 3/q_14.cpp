#include<iostream>
using namespace std;

void findValues(int a,int b,int c,int* largest,int* smallest){
    *largest=a;
    *smallest=a;
    if(b>*largest){
        *largest=b;
    }
    if(c>*largest){
        *largest=c;
    }
    if(b<*smallest){
        *smallest=b;
    }
    if(c<*smallest){
        *smallest=c;
    }
}

int main(){
    int a,b,c,largest,smallest;
    cout<<"Enter three integers: ";
    cin>>a>>b>>c;
    findValues(a,b,c,&largest,&smallest);
    cout<<"Largest: "<<largest<<endl;
    cout<<"Smallest: "<<smallest;
    return 0;
}