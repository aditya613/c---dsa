//Problem Statement: Given a number ‘N’, find out the sum of the first N natural numbers .

// Input: N=5
// Output: 15
// Explanation: 1+2+3+4+5=15

// Input: N=6
// Output: 21
// Explanation: 1+2+3+4+5+6=15


//parametrized way of recursive function
#include<bits/stdc++.h>
using namespace std;
void sum_numbers(int n, int sum){
    if(n==0){ cout<<sum;
     return;
    }

    sum_numbers(n-1, sum+n);
}
int main(){
    int n;
    cin>>n;
    sum_numbers(n, 0);
}


//functional way
//i.e the function only calculates the required and returns the value oinstead of printing itself

#include<bits/stdc++.h>
using namespace std;
int sum_numbers(int n){
    if(n==0) return 0;

    return n+sum_numbers(n-1);
}
int main(){
    int n;
    cin>>n;
    cout<<sum_numbers(n);

    return 0;
}