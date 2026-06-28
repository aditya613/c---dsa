// Example 1:
// Input: N = 6, array[] = {13,46,24,52,20,9}
// Output: 9,13,20,24,46,52
// Explanation: After sorting the array is: 9, 13, 20, 24, 46, 52

// Example 2:
// Input: N=5, array[] = {5,4,3,2,1}
// Output: 1,2,3,4,5
// Explanation: After sorting the array is: 1, 2, 3, 4, 5


#include<bits/stdc++.h>
using namespace std;

void selection_sort(int arr[], int n){


    for(int i=0;i<n-1;i++){
        int min = i;
        for(int j=i;j<n;j++){
            if(arr[j]<arr[min]){
                min = j;
            }

        }

        //swap the min with i'th position element
        int temp = arr[i];
        arr[i] = arr[min];
        arr[min] = temp;

    }

}

int main(){
    int n;
    cin>>n;
    int arr[n];
    for(int i=0;i<n;i++){
        cin>>arr[i];
    }

    selection_sort(arr, n);

    for(int i = 0; i < n; i++){
        cout << arr[i] << " ";
    }
    return 0;
}