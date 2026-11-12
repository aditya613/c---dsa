//my naive brute force 

#include<bits/stdc++.h>
using namespace std;

class Solution
{
public:
    int celebrity(vector<vector<int>> &M){

        int n = M.size();
        vector<int> intro;

        // Step 1: Find potential celebrities
        for(int i = 0; i < n; i++){
            bool knowsAnyone = false;
            for(int j = 0; j < n; j++){
                if(i != j && M[i][j] == 1){
                    knowsAnyone = true;
                    break;
                }
            }
            if(!knowsAnyone)
                intro.push_back(i);
        }
        // Step 2: Verify potential celebrities
        for(int i = 0; i < intro.size(); i++){
            bool knownByEveryone = true;
            for(int j = 0; j < n; j++){
                if(i != j && M[j][intro[i]] == 0){
                    knownByEveryone = false;
                    break;
                }
            }
            if(knownByEveryone)
                return intro[i];
        }
        return -1;
    }
};




//two pointer approach

class Solution {
public:
    int celebrity(vector<vector<int>>& M) {

        int n = M.size();

        // Step 1: Find potential celebrity
        int top = 0;
        int down = n - 1;

        while(top < down) {

            if(M[top][down] == 1) {
                top++;
            }
            else {
                down--;
            }
        }

        // Step 2: Verify the candidate
        int candidate = top;

        for(int i = 0; i < n; i++) {

            if(i == candidate)
                continue;

            // Candidate should know nobody
            // Everyone should know candidate
            if(M[candidate][i] == 1 ||
               M[i][candidate] == 0) {
                return -1;
            }
        }

        return candidate;
    }
};
