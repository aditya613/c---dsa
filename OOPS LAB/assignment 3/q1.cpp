#include<bits/stdc++.h>
using namespace std;
int search(int arr[], int n, int key){
    for(int i=0;i<n;i++){
        if(arr[i]==key){
            return i;
        }
        
    }

    return -1;

}
int main(){

    int n;
    cout<<"Enter size of array: ";
    cin>>n;

    cout<<"Enter "<<n<<"numbers separated by space: ";
    int arr[n];
    for(int i=0;i<n;i++){
        cin>>arr[i];
    }

    cout<<"Enter Element u find to find: ";
    int key;
    cin>>key;

    cout<<"Result: "<<search(arr, n, key);
}