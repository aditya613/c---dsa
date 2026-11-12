#include<bits/stdc++.h>
using namespace std;

int main(){
    int t;
    cin>>t;
    while(t--){
        int n;
        cin>>n;
        string s;
        cin>>s;

        vector<int> diff(27, -1);

        int left = 0;
        int right = n-1;

        while(left<right){
            int itiDiff = s[left] - s[right];
            if(diff[s[left]-'a']==-1){
                diff[s[left]-'a'] = itiDiff;
            }
            else if(diff[s[left]-'a']==itiDiff || diff[s[left]-'a']==-2){
                continue;
            }
            else{
                diff[s[left]-'a']==-2;
            }
            
            left++;
            right--;
        }

        int operations = 0;
        for(int i=0;i<diff.size();i++){
            if(diff[i] != -1 && diff[i] !=-2){
                operations+=abs(diff[i]);
            }
        }

        cout<<operations<<'\n';

    }

    return 0;
}