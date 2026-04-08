// Example 1:
// Input:N = 153
// Output:True
// Explanation: 1^3+5^3+3^3 = 1 + 125 + 27 = 153
                                        
// Example 2:
// Input:N = 371                
// Output: True
// Explanation: 3^3+7^3+1^3 = 27 + 343 + 1 = 371
            
bool check_armstrong(int n);
#include<bits/stdc++.h>
using namespace std;
int main(){
    int n;
    cin>>n;
    cout<<check_armstrong(n);
    return 0;

}

bool check_armstrong(int n){
    int original = n;
    int sum=0;

    while(n!=0){
        sum += (n%10)*(n%10)*(n%10);
        
        n/=10;
    }

    if(original==sum) return true;
    
    return false;
}