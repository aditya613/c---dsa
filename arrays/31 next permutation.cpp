// 31. Next Permutation
// Medium
// Topics
// premium lock icon
// Companies
// A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

// For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
// The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

// For example, the next permutation of arr = [1,2,3] is [1,3,2].
// Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
// While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
// Given an array of integers nums, find the next permutation of nums.

// The replacement must be in place and use only constant extra memory.

 

// Example 1:

// Input: nums = [1,2,3]
// Output: [1,3,2]
// Example 2:

// Input: nums = [3,2,1]
// Output: [1,2,3]
// Example 3:

// Input: nums = [1,1,5]
// Output: [1,5,1]
 

// Constraints:

// 1 <= nums.length <= 100
// 0 <= nums[i] <= 100


//brute force solution
#include<bits/stdc++.h>
using namespace std;

void getPermutation(int index, vector<int>& nums, vector<vector<int>>& ans){

    if(index==nums.size()-1){
        ans.push_back(nums);
        return;
    }


    for(int i=index;i<nums.size();i++)
    {
        swap(nums[index], nums[i]);
        getPermutation(index+1, nums, ans);
        swap(nums[i], nums[index]);
    }
}

int main(){

    vector<int> nums_original = {1,1,5};
    vector<vector<int>> ans;


    //generate all permutations
    getPermutation(0, nums_original, ans);

    vector<int> trueAns;
    sort(ans.begin(), ans.end());
    //linear search the current permutation
    for(int i=0;i<ans.size();i++){
        if(ans[i]==nums_original){
            if(i==ans.size()-1){
                trueAns=(ans[0]);
            }
            else{
                trueAns=(ans[i+1]);
            }
        }
    }

    for(auto it:trueAns){
        cout<<it;
    }


}