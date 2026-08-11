// 796. Rotate String
// Solved
// Easy
// Topics
// premium lock icon
// Companies
// Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.

// A shift on s consists of moving the leftmost character of s to the rightmost position.

// For example, if s = "abcde", then it will be "bcdea" after one shift.
 

// Example 1:

// Input: s = "abcde", goal = "cdeab"
// Output: true
// Example 2:

// Input: s = "abcde", goal = "abced"
// Output: false
 

//brute force
//generate all rotated strings and check with goal

class Solution {
public:
    bool rotateString(string s, string goal) {
        

        if(s.size()!=goal.size()){
            return false;
        }
        
        if(s==goal){
            return true;
        }

        for(int i=0;i<s.size();i++){

            char temp = s[0];
            for(int j=0;j<s.size()-1;j++){
                swap(s[j], s[j+1]);
            }
            s[s.size()-1] = temp;

            if(s==goal){
                return true;
            }
        }

        return false;
    }
};

//O(N^2) time complexity


//optimal approach
class Solution {
public:
    bool rotateString(string s, string goal) {
        return s.size() == goal.size() &&
               (s + s).find(goal) != string::npos;
    }
};