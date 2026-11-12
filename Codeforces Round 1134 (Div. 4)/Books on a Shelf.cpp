#include<bits/stdc++.h>
using namespace std;


// int visibleFromLeft(vector<int> &heights, int n){
//     stack<int> st;
//     int visible = 0;
//     for(int i=0;i<n;i++){
//         while(!st.empty() && st.top()<heights[i]){
//             st.pop();
//         }
    
//     if(st.empty()) visible++;
//     st.push(heights[i]);

//     }

//     return visible;

// }

int main(){
    int t;
    cin>>t;

    while(t--){
        int n;
        cin>>n;
        vector<int> heights(n);

        for(int i=0;i<n;i++){
            cin>>heights[i];
        }

        sort(heights.begin(), heights.end());
        vector<int> arranged(n);
        arranged[0] = heights[0];

        int curr = 1;
        for(int i=1;i<n;i++){
            if(heights[i]!=arranged[curr-1]){
                arranged[curr] = heights[i];
                heights[i] = -1;
                curr++;
            }
        }

        sort(heights.rbegin(), heights.rend());

        int visibleFromLeft = curr;
        int visibleFromRight = 0;
        for(int i=curr;i<n;i++){
            arranged[i] = heights[i-curr];
            if(arranged[i-1]!=arranged[i]) visibleFromRight++;
        }

        if(arranged[curr]==arranged[curr-1]) visibleFromRight

        

        cout<<visibleFromLeft+visibleFromRight<<"\n";
        for(int i=0;i<n;i++){
            cout<<arranged[i]<<" ";
        }
        cout<<"\n";

        //cout<<visibleFromLeft(heights, n);

    }

    return 0;
}