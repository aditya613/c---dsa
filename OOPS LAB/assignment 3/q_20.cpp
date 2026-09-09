#include<iostream>
using namespace std;

int removeDuplicates(int* arr,int n){
    for(int i=0;i<n;i++){
        for(int j=i+1;j<n;j++){
            if(arr[i]==arr[j]){
                for(int k=j;k<n-1;k++){
                    arr[k]=arr[k+1];
                }
                n--;
                j--;
            }
        }
    }
    return n;
}

void display(int* arr,int n){
    for(int i=0;i<n;i++){
        cout<<arr[i]<<" ";
    }
}

int main(){
    int arr[8]={2,5,2,7,5,8,7,9};
    int n=8;
    cout<<"Original array: ";
    display(arr,n);
    n=removeDuplicates(arr,n);
    cout<<"\nModified array: ";
    display(arr,n);
    cout<<"\nNew size: "<<n;
    return 0;
}