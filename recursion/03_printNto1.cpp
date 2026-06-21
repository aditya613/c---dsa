//Print N to 1 using Recursion
// Input: N = 4
// Output: 4, 3, 2, 1
// Explanation: All the numbers from 4 to 1 are printed.
// Input: N = 1
// Output: 1 
// Explanation: This is the base case.

#include<bits/stdc++.h>
using namespace std;
void print_number(int n){
    if(n==0) return;
    cout<<n<< " ";

    print_number(--n);
}
int main(){
    int n;
    cin>>n;
    print_number(n);
}