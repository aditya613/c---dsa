#include<iostream>
using namespace std;
int* increaseSize(int* arr,int n){
    int* newArr=new int[2*n];
    for(int i=0;i<n;i++){
        newArr[i]=arr[i];
    }
    delete[] arr;
    return newArr;
}
void display(int* arr,int n){
    for(int i=0;i<n;i++){
        cout<<arr[i]<<" ";
    }
}
int main(){
    int n;
    cout<<"Enter size: ";
    cin>>n;
    int* arr=new int[n];
    cout<<"Enter "<<n<<" elements: ";
    for(int i=0;i<n;i++){
        cin>>arr[i];
    }
    cout<<"Original array: ";
    display(arr,n);
    arr=increaseSize(arr,n);
    cout<<"\nEnter "<<n<<" additional elements: ";
    for(int i=n;i<2*n;i++){
        cin>>arr[i];
    }
    n=2*n;
    cout<<"Array after increasing size: ";
    display(arr,n);
    delete[] arr;
    return 0;
}