//Problem Description: Given an integer N, write a program to print your name N times.
// Input: N = 3
// Output: Ashish Ashish Ashish 
// Explanation: Name is printed 3 times.
// Input: N = 1
// Output: Ashish 
// Explanation: Name is printed once.

#include<bits/stdc++.h>
using namespace std;

void print_name(int n){
    cout<<"Aditya";
    n--;
    if(n==0) return;
    else print_name(n);
}

int main(){
    int n;
    cin>>n;
    print_name(n);
}