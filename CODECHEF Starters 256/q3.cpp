#include <bits/stdc++.h>
using namespace std;

int main() {
	
    int t;
    cin>>t;
    while(t--){
        int N,K;
        cin>>N>>K;

        if(N==1 && K==0){
            cout<<"No";
        }
        else{
        cout<<((K==N-1)?"No":"Yes");
        }
        cout<<endl;


    }

}

