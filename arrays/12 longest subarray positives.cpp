// Longest Subarray with given Sum K(Positives)


// 41

// Problem Statement: Given an array nums of size n and an integer k, find the length of the longest sub-array that sums to k. If no such sub-array exists, return 0.

// Examples
// Example 1:
// Input:
//  nums = [10, 5, 2, 7, 1, 9], k = 15  
// Output:
//  4  
// Explanation:
//  The longest sub-array with a sum equal to 15 is [5, 2, 7, 1], which has a length of 4. This sub-array starts at index 1 and ends at index 4, and the sum of its elements (5 + 2 + 7 + 1) equals 15. Therefore, the length of this sub-array is 4.

// Example 2:
// Input:
//  nums = [-3, 2, 1], k = 6  
// Output:
//  0  
// Explanation:
//  There is no sub-array in the array that sums to 6. Therefore, the output is 0.


#include<bits/stdc++.h>
using namespace std;


// M-1 brute force

int subarraySum(vector<int>& nums, int k) {
        

        int numSubArray = 0;

        for(int i=0;i<nums.size();i++){

            int sum = 0;
            for(int j=i; j<nums.size();j++){

                sum+=nums[j];
                if(sum==k){
                    numSubArray+=1;
                }


            }

        }
        return numSubArray;
    }


//M-2 


int main(){

int left=0, right=1, sum=arr[0];
int maxLen = 0;

while(right<arr.size()){

    if(sum>k){
        sum-=arr[left];
        left+=1;
    }
    else if(sum<k){
        if(right==arr.size()-1){
right+=1;
        }
        else{
            right+=1;
            
        sum+=arr[right];
        }
    }
    
    else{
        
        if(right==arr.size()-1){
right+=1;
        }
        else{
            right+=1;
            
        sum+=arr[right];
        }
    }
}
return maxLen


}

