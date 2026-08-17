#include<bits/stdc++.h>
using namespace std;

bool is_prime(int n){
    for(int i=2;i<n;i++){
        if(n%i==0){
            return false;
        }
    }

    return true;
}
int main(){

    vector<int> primes;

    int i=100;
    while(true){
        if(is_prime(i)){
            primes.push_back(i);
            i++;
        }
        else{
            i++;
            continue;
        }

        if(primes.size()==5){
            break;
        }

        
    }

    for(auto i:primes){
        cout<<i<<endl;
    }
}