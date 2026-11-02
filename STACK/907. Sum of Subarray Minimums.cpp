#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> nse(vector<int>& arr){
        vector<int> ans;
        stack<int> st;
        for(int i=arr.size()-1;i>=0;i--){
            
            while(!st.empty() && arr[st.top()]>=arr[i]){
                st.pop();
            }

            if(!st.empty()) ans.push_back(i);
            else ans.push_back(-1);

        }
        return ans;

    } 

    vector<int> pse(vector<int>& arr){

        vector<int> ans;
        stack<int> st;
        for(int i=1;i<arr.size();i++){
            
            while(!st.empty() && arr[st.top()]>=arr[i]){
                st.pop();
            }

            if(!st.empty()) ans.push_back(i);
            else ans.push_back(-1);

            
        }

        return ans;

    } 
    int sumSubarrayMins(vector<int>& arr) {
        int n = arr.size();
        long long sum = 0;
        int mod = 1e9 + 7;

        vector<int> pseArr = pse(arr);
        vector<int> nseArr = nse(arr);

        for(int i=0;i<n;i++){

            int left = 0;
            int right = 0;
            (pseArr[i]==-1) ? left = 1: left = i-pseArr[i];

            (nseArr[i]==-1) ? right = 1: right = nseArr[i]-i;

            sum  = (sum + (left*right*1LL*arr[i])%mod) % mod;
            
        }
        return sum;
    }
};
