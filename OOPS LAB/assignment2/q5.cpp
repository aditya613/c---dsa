#include<bits/stdc++.h>
using namespace std;
int main(){
    int a,b;
    cout<<"Enter first num: ";
    cin>>a;

    cout<<"Enter second num: ";
    cin>>b;
    for(int i=1;i<=1000;i++){
        if (i % a == 0 && i % b == 0) {
            cout<<i<<" is the first num divisible by both";
            return 0;
        }
    }
    cout<<"No num from 1 to 1000 divisble by both";
    return 0;
}