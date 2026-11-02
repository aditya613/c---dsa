#include <bits/stdc++.h>
using namespace std;

int main() {
	
	int t;
	cin>>t;
	
	while(t--){
	    int n;
	    cin>>n;
	    
	    string s;
	    cin>>s;
	    
	    char current;
	    int count = 0;
	    current = s[0];
	    int ans = 0;
	    for(int i=0;i<n;i++){
	        
	        if(s[i] == current)
	            count++;
	       else{
	       
	            current = s[i];
	            count = 1;
	       }
	       
	       if(count == 3){
	           count = 0;
	           ans++;
	       }
	    }
	    
	    cout<<ans<<endl;
	}
	
	return 0;

}
