// Given an integer x, return true if x is a palindrome, and false otherwise.

 

// Example 1:

// Input: x = 121
// Output: true
// Explanation: 121 reads as 121 from left to right and from right to left.
// Example 2:

// Input: x = -121
// Output: false
// Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
// Example 3:

// Input: x = 10
// Output: false
// Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

#include<bits/stdc++.h>
using namespace std;

bool check_palindrome(int n);
int main(){
    int n;
    cin>>n;

    cout<<check_palindrome(n);
    return 0;

}

bool check_palindrome(int n){

    int original;
    original = n;
    if(n<0)return false;

    int rev_num=0;
    while(n>0){
        rev_num = (rev_num*10)+n%10;
        n/=10;
    }

    if(rev_num==original){
        return true;
    }else{
        return false;
    }
}