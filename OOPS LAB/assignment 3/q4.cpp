#include<bits/stdc++.h>
using namespace std;

void reverseArray(vector<int>& arr, int start, int end){
    while(start < end)
{
    swap(arr[start], arr[end]);
    start++;
    end--;
}
}
vector<int> rotateArray(vector<int> arr, int k){
    int n = arr.size();

    if(k>n){
            k =k%n;
    }
    reverseArray(arr, 0, n-k-1);
    reverseArray(arr, n-k, n-1);
    reverseArray(arr,0,n-1);

    return arr;
}   

int main(){

    int n;
    cout<<"Enter Size of Array: ";
    cin>>n;

    vector<int> arr(n);
    
    for(int i=0;i<n;i++){
        cin>>arr[i];
    }

    cout<<"Enter K: ";
    
    int k;
    cin>>k;
    cout<<endl<<endl;

    cout<<"BEFORE ARRAY: "<<endl;
    for(int i=0;i<n;i++){
        cout<<arr[i]<<" ";
    }
    cout<<endl<<"AFTER ARRAY: "<<endl;
    vector<int> rotatedArray = rotateArray(arr, k);
    for(int i=0;i<n;i++){
        cout<<rotatedArray[i]<<" ";
    }


}