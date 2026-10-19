#include<bits/stdc++.h>
using namespace std;

//brute force solution
class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        int maxArea = 0;

        for(int i=0;i<heights.size();i++){
            int height = heights[i];

            int left = i;

            while(left>=0 && heights[left] >= height)
                left--;

            int right = i;
            while(right<heights.size() && heights[right] >= height)
                right++;

            maxArea = max(maxArea, height * (right-left-1));
        }

        return maxArea;
    }
};