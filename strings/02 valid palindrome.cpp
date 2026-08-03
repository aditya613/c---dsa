#include<bits/stdc++.h>
using namespace std;

void cleanString(string& s) {
        
        for (char c : s) {
            if (isalnum(c)) {
                c = tolower(c);
            }
        }
        
    }


int main(){
    string s;
    cin>>s;


    cleanString(s);

    int left=0, right= s.size()-1;

    while(left<=right){
        if(s[left]!=s[right]){
            cout<<false;
            return 0;
        }
        left++;
        right--;
    }

    cout<<true;
    return 0;
}