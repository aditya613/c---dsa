#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    vector<int> maxSubArray(vector<int>& nums) {
        

        long long sum = 0;
        long long maxi = nums[0];
        int start=0, end=0;
          int temp_start = 0;

        for(int i=0;i<nums.size(); i++){

            sum+=nums[i];
            
              if (sum > maxi) {
                maxi = sum;
                start = temp_start;
                end = i;
            }

          
            
            
            if(sum<0){
                sum = 0;
                temp_start = i + 1;            
            }
        }

        auto it = nums.begin() + start;
        auto it_end = nums.begin() + end;

        vector<int> slice(it, it_end+1);
        return slice;
    }
};



int main(){

    Solution sol1;

    vector<int> nums = {2,3,5,6,1,4,2,-3,5,-2,-2,-1};

    nums = sol1.maxSubArray(nums);

    int sum=0;
    for(auto it:nums){
        cout<<(it)<<endl;
        sum+=it;
    }
    cout<<sum;
}