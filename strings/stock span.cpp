#include<bits/stdc++.h>
using namespace std;

int main(){

    int arr[] = {100,80,60,70,60,75,85};

    int n = sizeof(arr) / sizeof(arr[0]);
    vector<int> ans(n, 1);

    stack<int> st;
    for(int i=0;i<n;i++){
        while(!st.empty() && arr[st.top()]<=arr[i]){
            st.pop();
        }

        if(!st.empty())ans[i] = st.top()-i;
        st.push(i);
    }
}