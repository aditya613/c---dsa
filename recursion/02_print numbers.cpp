//Problem Description: Given an integer N, write a program to print numbers from 1 to N.

#include<bits/stdc++.h>
using namespace std;

void print_number(int start, int n){
        
    if(start>n) return;
    
    cout<<start;
    start++;
    print_number(start, n);

}
int main(){
    int n;
    cin>>n;
    print_number(1,n);
}
