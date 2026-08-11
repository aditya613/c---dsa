// 14. Longest Common Prefix
// Solved
// Easy
// Topics
// premium lock icon
// Companies
// Write a function to find the longest common prefix string amongst an array of strings.

// If there is no common prefix, return an empty string "".

 

// Example 1:

// Input: strs = ["flower","flow","flight"]
// Output: "fl"
// Example 2:

// Input: strs = ["dog","racecar","car"]
// Output: ""
// Explanation: There is no common prefix among the input strings.



//brute force
// generating all possible prefixes and hashing their frequency
// class Solution {
// public:
//     string longestCommonPrefix(vector<string>& strs) {
//         unordered_map<string, int> ans;

//         for(auto i:strs){
//             for(int j=1;j<=i.size();j++){

//                     string temp;
//                     temp = i.substr(0, j);
//                     ans[temp]++;
//             }
//         }

//         string maxi = "";
//         for(auto i:ans){
//             if(i.first.size()>maxi.size() && i.second==strs.size()){
//                 maxi = i.first;
//             }
//         }

//         return maxi;
//     }
// };



#include<bits/stdc++.h>
using namespace std;

int main(){
    
}