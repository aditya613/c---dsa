#include<iostream>
using namespace std;

int* allocate(int n){
    return new int[n];
}
void readArray(int* arr,int n){
    for(int i=0;i<n;i++){
        cin>>arr[i];
    }
}
void display(int* arr,int n){
    for(int i=0;i<n;i++){
        cout<<arr[i]<<" ";
    }
}
void deallocate(int*& arr){
    delete[] arr;
}
int main(){
    int n;
    cout<<"Enter n: ";
    cin>>n;
    int* arr=allocate(n);
    cout<<"Enter elements: ";
    readArray(arr,n);
    cout<<"Array: ";
    display(arr,n);
    deallocate(arr);
    cout<<"\nAfter delete, pointer still contains an address: "<<arr<<endl;
    cout<<"Accessing arr[0] after delete gives undefined behavior."<<endl;
    arr=nullptr;
    cout<<"After setting pointer to nullptr: "<<arr<<endl;
    return 0;
}