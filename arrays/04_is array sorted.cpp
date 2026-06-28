// //1752. Check if Array Is Sorted and Rotated
// Given an array nums, return true if the array was originally sorted in non-decreasing order, then rotated some number of positions (including zero). Otherwise, return false.

// There may be duplicates in the original array.

// Note: An array A rotated by x positions results in an array B of the same length such that B[i] == A[(i+x) % A.length] for every valid index i.

 

// Example 1:

// Input: nums = [3,4,5,1,2]
// Output: true
// Explanation: [1,2,3,4,5] is the original sorted array.
// You can rotate the array by x = 2 positions to begin on the element of value 3: [3,4,5,1,2].

//my solution 

#include<bits/stdc++.h>
using namespace std;


bool check(vector<int>& nums) {
    int index = 0;
    for(int i=1; i<nums.size(); i++){

        if(nums.at(i)<nums.at(i-1)){
            index = i;
        }
    }

    //form original array

    vector<int> original;
    for(int i=index;i<nums.size();i++){
    original.push_back(nums.at(i));
    }
    for(int i=0;i<index;i++){
        original.push_back(nums.at(i));
    }

        for(int i=1; i<original.size(); i++){

        if(original.at(i)<original.at(i-1)){
            return false;
        }
    }
    return true;
}

void main(){

    vector<int> nums = {3,4,5,1,20};
    cout<<check(nums);
}