#include<iostream>
using namespace std;

int sum(int* arr,int n,int start=0,int end=-1){
    if(end==-1){
        end=n-1;
    }
    int s=0;
    for(int i=start;i<=end;i++){
        s=s+arr[i];
    }
    return s;
}

int main(){
    int arr[6]={10,20,30,40,50,60};
    int n=6;
    cout<<"Sum with no positions: "<<sum(arr,n)<<endl;
    cout<<"Sum from position 2: "<<sum(arr,n,2)<<endl;
    cout<<"Sum from position 1 to 4: "<<sum(arr,n,1,4);
    return 0;
}