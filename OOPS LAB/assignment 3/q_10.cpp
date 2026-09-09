#include<iostream>
using namespace std;

int findOdd(int* arr,int n){
    int result=0;
    for(int i=0;i<n;i++){
        result=result^arr[i];
    }
    return result;
}

int main(){
    int arr[7]={2,5,2,5,5,5,5};
    int n=7;
    cout<<"Odd occurring element: "<<findOdd(arr,n);
    return 0;
}