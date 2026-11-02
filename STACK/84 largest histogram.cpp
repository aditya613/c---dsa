#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> pseArray(vector<int>& h) {
        int n = h.size();
        vector<int> ans(n);
        stack<int> st;
        for (int i = 0; i < n; i++) {
            while (!st.empty() && h[st.top()] >= h[i]) st.pop();
            ans[i] = st.empty() ? -1 : st.top();
            st.push(i);
        }
        return ans;
    }

    vector<int> nseArray(vector<int>& h) {
        int n = h.size();
        vector<int> ans(n);
        stack<int> st;
        for (int i = n - 1; i >= 0; i--) {
            while (!st.empty() && h[st.top()] >= h[i]) st.pop();
            ans[i] = st.empty() ? n : st.top();
            st.push(i);
        }
        return ans;
    }

    int largestRectangleArea(vector<int>& h) {
        vector<int> pse = pseArray(h), nse = nseArray(h);
        int maxArea = 0;
        for (int i = 0; i < (int)h.size(); i++)
            maxArea = max(maxArea, h[i] * (nse[i] - pse[i] - 1));
        return maxArea;
    }
};

int main(){
    
}