#include<bits/stdc++.h>
using namespace std;

int main(){

    int sum = 0;
    while(true){
        cout<<"Enter number: ";
        int temp;
        cin>>temp;

        if(temp==0){
            continue;
        }
        else if(temp<0){
            break;
        }

        sum+=temp;
    }

    cout<<"Sum calculates till now is "<<sum;
}