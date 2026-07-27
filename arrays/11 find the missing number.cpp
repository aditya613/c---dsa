
// Find the Missing Number
// Last Updated : 19 Apr, 2025
// Given an array arr[] of size n-1 with distinct integers in the range of [1, n]. This array represents a permutation of the integers from 1 to n with one element missing. Find the missing element in the array.

// Examples: 

// Input: arr[] = [8, 2, 4, 5, 3, 7, 1]
// Output: 6
// Explanation: All the numbers from 1 to 8 are present except 6.

// Input: arr[] = [1, 2, 3, 5]
// Output: 4
// Explanation: Here the size of the array is 4, so the range will be [1, 5]. The missing number between 1 to 5 is 4



#include<bits/stdc++.h>
using namespace std;

int missingNumber(int arr1[], int n){

    //M-1
    // sort(arr1, arr1+n);
    // int i=0;
    // while(i<n-1){
    //     if(arr1[i] != (arr1[i+1]-1)){
    //         return arr1[i]+1;
    //     }
    //     i++;

    // }


    
}

int main(){

    int arr[] = {1,2,3,5};
    cout<< missingNumber(arr, (sizeof(arr)/sizeof(arr[0])));

}