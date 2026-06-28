// Example 1:
// Input: N = 5, array[] = {5,4,3,2,1}
// Output: 1,2,3,4,5
// Explanation: After sorting we get 1,2,3,4,5


// Example 2:
// Input: N = 6, array[] = {13,46,24,52,20,9}
// Output: 9,13,20,24,46,52
// Explanation: After sorting we get 9,13,20,24,46,52
            
#include<bits/stdc++.h>
using namespace std;

void bubble_sort(int arr[], int n){


    for(int i=n-1;i>=0;i--){

        for(int j=0;j<i;j++){

            if(arr[j]>arr[j+1]){

                int temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }


    }

}

int main(){
    int n;
    cin>>n;
    int arr[n];
    for(int i=0;i<n;i++){
        cin>>arr[i];
    }

    bubble_sort(arr, n);

    for(int i=0;i<n;i++){
        cout<<arr[i]<<" ";
    }

    return 0;


}