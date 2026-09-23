#include <bits/stdc++.h>
using namespace std;

int main() {
	

    int t;
    cin>>t;
    while(t--){
        int N, K;
        cin>>N>>K;

        if(K>N){
            cout<< 2*(K-N)<<endl;
        }
        else{
            cout<<0<<endl;
        }
    }
}
