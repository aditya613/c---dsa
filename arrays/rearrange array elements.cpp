// 2149. Rearrange Array Elements by Sign
// Solved
// Medium
// Topics
// premium lock icon
// Companies
// Hint
// You are given a 0-indexed integer array nums of even length consisting of an equal number of positive and negative integers.

// You should return the array of nums such that the array follows the given conditions:

// Every consecutive pair of integers have opposite signs.
// For all integers with the same sign, the order in which they were present in nums is preserved.
// The rearranged array begins with a positive integer.
// Return the modified array after rearranging the elements to satisfy the aforementioned conditions.


//brute force - O(2n) using 2 passes

class Solution {
public:
    vector<int> rearrangeArray(vector<int>& nums) {
        
        vector<int> pos;
        vector<int> neg;

        for(int i=0;i<nums.size();i++){
            if(nums[i]<0){
                neg.push_back(nums[i]);
            }
            else{
                pos.push_back(nums[i]);
            }
        }

        for(int i=0;i<nums.size()/2;i++){
            nums[2*i] = pos[i];
            nums[2*i+1] = neg[i];
        }

        return nums;
    }
};


//most optimal one pass solution

class Solution {
public:
    vector<int> rearrangeArray(vector<int>& nums) {
        
        int pos=0;
        int neg=1;
        vector<int> modNums(nums.size());
        for(int i=0;i<nums.size();i++){
            if(nums[i]<0){
               modNums[neg] = nums[i];
               neg+=2;
            }
            else{
                modNums[pos] = nums[i];
                pos+=2;
            }
        }
            

        return modNums;
    }
};