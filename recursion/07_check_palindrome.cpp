//Problem Statement: Given a string, check if the string is palindrome or not. A string is said to be palindrome if the reverse of the string is the same as the string.

// Example 1:
// Input: Str =  “ABCDCBA”
// Output: Palindrome
// Explanation: String when reversed is the same as string.

// Example 2:
// Input: Str = “TAKE U FORWARD”
// Output: Not Palindrome
// Explanation: String when reversed is not the same as string.

#include<bits/stdc++.h>
#include<conio.h>

using namespace std;

bool check_palindrome(string &s, int n){

    if(n>=s.size()/2){
        return true;
    }

    if(s[n]!=s[s.size()-n-1]) return false;

    return check_palindrome(s, n+1);

}

int main(){
   
    string s;
    cin>>s;

    cout<<check_palindrome(s,0);
getch();

}