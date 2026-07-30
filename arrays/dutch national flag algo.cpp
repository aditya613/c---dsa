// Sort an array of 0s, 1s and 2s


// 26

// Problem Statement: Given an array nums consisting of only 0, 1, or 2. Sort the array in non-decreasing order. The sorting must be done in-place, without making a copy of the original array.

// Examples
// Input: nums = [1, 0, 2, 1, 0]
// Output: [0, 0, 1, 1, 2]
// Explanation: The nums array in sorted order has 2 zeroes, 2 ones and 1 two

// Input: nums = [0, 0, 1, 1, 1]
// Output: [0, 0, 1, 1, 1]
// Explanation: The nums array in sorted order has 2 zeroes, 3 ones and zero twos.


class Solution {
public:
    void sortColors(vector<int>& nums) {

        int low=0, mid=0, high=nums.size()-1;

        while(mid<=high){
            int temp;
            if(nums[mid]==0){
                temp = nums[mid];
                nums[mid] = nums[low];
                nums[low] = temp;

                low++;
                mid++;
            }
            else if(nums[mid]==1){
                mid++;
            }
            else{
                temp = nums[mid];
                nums[mid] = nums[high];
                nums[high] = temp;

                high--;
            }


        }



    }


};