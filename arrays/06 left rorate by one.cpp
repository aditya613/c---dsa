// Left Rotate the Array by One


// 21

// Problem Statement: Given an integer array nums, rotate the array to the left by one.

// Note: There is no need to return anything, just modify the given array.

// Examples
// Example 1:
// Input:
//  nums = [1, 2, 3, 4, 5]  
// Output:
//  [2, 3, 4, 5, 1]  
// Explanation:
//  Initially, nums = [1, 2, 3, 4, 5]  
// Rotating once to the left results in nums = [2, 3, 4, 5, 1].

// Example 2:
// Input:
//  nums = [-1, 0, 3, 6]  
// Output:
//  [0, 3, 6, -1]  
// Explanation:
//  Initially, nums = [-1, 0, 3, 6]  
// Rotating once to the left results in nums = [0, 3, 6, -1].


#include<bits/stdc++.h>
using namespace std;
int main(){

    vector<int> nums = {1,2,8,4,6,9};

    int temp = nums[0];
    for(int i=1;i<nums.size();i++){
        nums[i-1]=nums[i];
    }

    nums[nums.size()-1]=temp;

    for(int i=0;i<nums.size();i++){
        cout<<nums[i];
    }

    return 0;
}