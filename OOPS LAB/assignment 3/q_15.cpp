#include<iostream>
using namespace std;

void modify(int* arr,int n){
    for(int i=0;i<n;i++){
        if(i%2==0){
            arr[i]=arr[i]*2;
        }
        else{
            arr[i]=arr[i]*3;
        }
    }
}

void display(int* arr,int n){
    for(int i=0;i<n;i++){
        cout<<arr[i]<<" ";
    }
}

int main(){
    int arr[6]={10,20,30,40,50,60};
    int n=6;
    cout<<"Original array: ";
    display(arr,n);
    modify(arr,n);
    cout<<"\nModified array: ";
    display(arr,n);
    return 0;
}