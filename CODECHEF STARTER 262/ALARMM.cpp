#include <bits/stdc++.h>
using namespace std;

int main() {
	
	int t;
	cin>>t;
	while(t--){
	    int n,k;
	    cin>>n>>k;
	    
	    string s;
	    cin>>s;
	    int ans=0;
	    while(n>0){
	        if(s[n-1]=='1'){
	            int skip = 1;
	            ans++;
	           n = max(1, n - k) - 1;

	            
	        }
	        else
	            n--;
	    }
	    
	    cout<<ans<<endl;
	}

}
