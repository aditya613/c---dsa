#include<iostream>
using namespace std;

int sum(int* arr,int n){
    int s=0;
    for(int i=0;i<n;i++){
        s=s+arr[i];
    }
    return s;
}
int maximum(int* arr,int n){
    int max=arr[0];
    for(int i=1;i<n;i++){
        if(arr[i]>max){
            max=arr[i];
        }
    }
    return max;
}
void display(int* arr,int n){
    for(int i=0;i<n;i++){
        cout<<arr[i]<<" ";
    }
}
int main(){
    int n;
    cout<<"Enter n: ";
    cin>>n;
    int* arr=new int[n];
    cout<<"Enter elements: ";
    for(int i=0;i<n;i++){
        cin>>arr[i];
    }
    cout<<"Array: ";
    display(arr,n);
    cout<<"\nSum: "<<sum(arr,n);
    cout<<"\nMaximum: "<<maximum(arr,n);
    delete[] arr;
    arr=nullptr;
    return 0;
}