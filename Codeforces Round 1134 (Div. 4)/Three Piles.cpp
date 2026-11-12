#include<bits/stdc++.h>
using namespace std;

int main(){
    int t;
    cin>>t;

    while(t--){
        int a,b,c;
        cin>>a>>b>>c;

        int s1 = min(a,min(b,c));
        int s3 = max(a, max(b,c));
        if((a+b+c)%3==0 && s3==s1+2) cout<<"YES\n";
        else cout<<"NO\n";
    }

    return 0;
}