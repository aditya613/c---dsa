#include<iostream>
using namespace std;

int frequency(int* arr,int n,int key){
    int count=0;
    for(int i=0;i<n;i++){
        if(arr[i]==key){
            count++;
        }
    }
    return count;
}

bool isAlreadyCounted(int* arr,int index,int key){
    for(int i=0;i<index;i++){
        if(arr[i]==key){
            return true;
        }
    }
    return false;
}

void displayFrequency(int* arr,int n){
    for(int i=0;i<n;i++){
        if(!isAlreadyCounted(arr,i,arr[i])){
            cout<<arr[i]<<" -> "<<frequency(arr,n,arr[i])<<endl;
        }
    }
}

int main(){
    int arr[8]={2,5,2,7,5,2,8,7};
    int n=8;
    displayFrequency(arr,n);
    return 0;
}