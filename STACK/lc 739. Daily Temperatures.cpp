class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        
        stack<int> st;

        vector<int> ans(temperatures.size(), 0);

        for(int i=temperatures.size()-1;i>=0;i--){
            int count = 0;
            while(!st.empty() && temperatures[st.top()]<=temperatures[i]){
                st.pop();
            }

            if(!st.empty()) ans[i] = st.top()-i;

            st.push(i);
        }

        return ans;
    }
};

// Time: \(O(n)\). Each index is pushed once and popped at most once.



// Auxiliary space: \(O(n)\) for the stack.