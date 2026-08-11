// 205. Isomorphic Strings
// Easy
// Topics
// premium lock icon
// Companies
// Given two strings s and t, determine if they are isomorphic.

// Two strings s and t are isomorphic if the characters in s can be replaced to get t.

// All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

 

// Example 1:

// Input: s = "egg", t = "add"

// Output: true

// Explanation:

// The strings s and t can be made identical by:

// Mapping 'e' to 'a'.
// Mapping 'g' to 'd'.
// Example 2:

// Input: s = "f11", t = "b23"

// Output: false

// Explanation:

// The strings s and t can not be made identical as '1' needs to be mapped to both '2' and '3'.

// Example 3:

// Input: s = "paper", t = "title"

// Output: true

 

// Constraints:

// 1 <= s.length <= 5 * 104
// t.length == s.length
// s and t consist of any valid ascii character.

//using unordered map DS we map the characters and check
class Solution {
public:
    bool isIsomorphic(string s, string t) {
        
        unordered_map<char, char> mpp;
        for(int i=0;i<s.size();i++){

            if(mpp.find(s[i])!=mpp.end()){
                if(mpp[s[i]] != t[i]){
                    return false;
                }
            }else{
                mpp[s[i]] = t[i];
            }
            
            
        }

        return true;
    }
};

//one issue in above
// This guarantees:

// one character in s cannot map to two different characters in t.

// But the problem also requires:

// two different characters in s cannot map to the same character in t.


//correct approach using maps 
class Solution {
public:
    bool isIsomorphic(string s, string t) {

        unordered_map<char, char> sToT;
        unordered_map<char, char> tToS;

        for(int i = 0; i < s.size(); i++) {

            if(sToT.count(s[i]) && sToT[s[i]] != t[i])
                return false;

            if(tToS.count(t[i]) && tToS[t[i]] != s[i])
                return false;

            sToT[s[i]] = t[i];
            tToS[t[i]] = s[i];
        }

        return true;
    }
};

// Time: O(n) average
// Space: O(1) in practice because the character set is bounded