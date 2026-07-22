// Union of Two Sorted Arrays


// 23

// Problem Statement: Given two sorted arrays, arr1, and arr2 of size n and m. Find the union of two sorted arrays.

// The union of two arrays can be defined as the common and distinct elements in the two arrays.

// NOTE: Elements in the union should be in ascending order.

// Examples

// Input:n = 5,m = 5 arr1[] = {1,2,3,4,5}  arr2[] = {2,3,4,4,5}
// Output: {1,2,3,4,5}
// Explanation: Common Elements in arr1 and arr2  are:  2,3,4,5
// Distnict Elements in arr1 are : 1
// Distnict Elemennts in arr2 are : No distinct elements.
// Union of arr1 and arr2 is {1,2,3,4,5}

// Input:n = 10,m = 7,arr1[] = {1,2,3,4,5,6,7,8,9,10}arr2[] = {2,3,4,4,5,11,12}
// Output: {1,2,3,4,5,6,7,8,9,10,11,12}
// Explanation: Common Elements in arr1 and arr2  are:  2,3,4,5
// Distnict Elements in arr1 are : 1,6,7,8,9,10
// Distnict Elemennts in arr2 are : 11,12
// Union of arr1 and arr2 is {1,2,3,4,5,6,7,8,9,10,11,12}


#include<bits/stdc++.h>
using namespace std;

vector<int> Union(int arr1[], int arr2[], int n, int m){


    int i=0, j=0;
    vector<int> temp;


    while(i<n && j<m){
        if(arr1[i]<=arr2[j]){
            if(temp.empty() || temp.back() != arr1[i]){
                temp.push_back(arr1[i]);
            }
            i++;
        }else{
             if(temp.empty() || temp.back() != arr2[j]){
                temp.push_back(arr2[j]);
            }
            j++;
        }
        }


    while(j<m){
          if(temp.empty() || temp.back() != arr2[j]){
                temp.push_back(arr2[j]);
            }
            j++;
    }
    while(i<n){
        if(temp.empty() || temp.back() != arr1[i]){
                temp.push_back(arr1[i]);
            }
            i++;
    }
    return temp;
}

int main(){


    int arr1[] = {1,2,3,4,5,5,6,7,8,8};
    int arr2[] = {2,3,4,5,6,7,8,9,9,10,11,12};


    vector<int> uni = Union(arr1,arr2,(sizeof(arr1)/sizeof(arr1[0])), (sizeof(arr2)/sizeof(arr2[0])));

    for(auto it : uni){
        cout<< it <<" ";
    }

    return 0;

}