#include<iostream>
using namespace std;

int* concatenate(int* arr1,int n1,int* arr2,int n2){
    int* arr3=new int[n1+n2];
    for(int i=0;i<n1;i++){
        arr3[i]=arr1[i];
    }
    for(int i=0;i<n2;i++){
        arr3[n1+i]=arr2[i];
    }
    return arr3;
}
void display(int* arr,int n){
    for(int i=0;i<n;i++){
        cout<<arr[i]<<" ";
    }
}
int main(){
    int n1,n2;
    cout<<"Enter size of first array: ";
    cin>>n1;
    cout<<"Enter size of second array: ";
    cin>>n2;
    int* arr1=new int[n1];
    int* arr2=new int[n2];
    cout<<"Enter first array: ";
    for(int i=0;i<n1;i++){
        cin>>arr1[i];
    }
    cout<<"Enter second array: ";
    for(int i=0;i<n2;i++){
        cin>>arr2[i];
    }
    int* arr3=concatenate(arr1,n1,arr2,n2);
    cout<<"Concatenated array: ";
    display(arr3,n1+n2);
    delete[] arr1;
    delete[] arr2;
    delete[] arr3;
    return 0;
}