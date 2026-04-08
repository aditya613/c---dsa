// Problem Statement: Given an integer N return the reverse of the given number.

// Note: If a number has trailing zeros, then its reverse will not include them. For e.g , reverse of 10400 will be 401 instead of 00401.
// Examples
// Input: N = 12345
// Output:54321
// Explanation: The reverse of 12345 is 54321.

// Input: N = 7789                
// Output: 9877
// Explanation: The reverse of number 7789 is 9877.

#include<bits/stdc++.h>
using namespace std;
int main(){
    int n;
    try{
    cin>>n;
    }
    catch(exception e){
        return 0;
    }

    int sign = (n<0)?-1:1;
    n = abs(n);
    int last_digit, rev_num=0;
    while(n>0){
        last_digit = n%10;
        n=(int)n/10;
        rev_num = (rev_num*10) + last_digit;
    }
    cout<<sign*rev_num;
    return sign*rev_num;
}