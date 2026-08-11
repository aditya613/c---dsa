// 151. Reverse Words in a String
// Medium
// Topics
// premium lock icon
// Companies
// Given an input string s, reverse the order of the words.

// A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

// Return a string of the words in reverse order concatenated by a single space.

// Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

 

// Example 1:

// Input: s = "the sky is blue"
// Output: "blue is sky the"
// Example 2:

// Input: s = "  hello world  "
// Output: "world hello"
// Explanation: Your reversed string should not contain leading or trailing spaces.
// Example 3:

// Input: s = "a good   example"
// Output: "example good a"
// Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
 

// Constraints:

// 1 <= s.length <= 104
// s contains English letters (upper-case and lower-case), digits, and spaces ' '.
// There is at least one word in s.

#include<bits/stdc++.h>
#include<string>
using namespace std;
// string reverseWords(string s) {
        
//     s+=' ';
//         vector<string> words;
//         string temp= "";

//         for(int i=0;i<s.size();i++){

//             if(s[i]!=' '){
//                 temp += s[i];
//             }
//             else if(temp.size()>=1){
//                 words.push_back(temp);
//                 temp = "";
//             }

           
//         }


//         temp = "";
//         for(int i=words.size()-1;i>=0;i--){
//             if(i==0){
//  temp += words[i];
//             }
//             else{
//         temp += words[i] + " ";
//         }
//         }

//         return temp;
//     }


string reverseWords(string s) {
        
        s+=' ';

        int start=0, end=0;
        string temp= "";
        string output= "";
        for(int i=0;i<s.size();i++){

           if(s[i]!=' '){
            temp = s.substr(i, s.size()-1);

            end = temp.find(' ');

            output += s.substr(i, end)+ " ";

            i=end;

           }
        }

        output = output.substr(0,output.size()-2);

        return output;

   }
int main(){

    string s = "the sky is blue";
    cout<<reverseWords(s);

    return 0;
}