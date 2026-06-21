//Factorial of a Number : Iterative and Recursive

// Example 1:
// Input:
//  X = 5
// Output:
//  120
// Explanation:
//  5! = 5*4*3*2*1

// Example 2:
// Input:
//  X = 3
// Output:
//  6
// Explanation:
//  3!=3*2*1


//iterative way
// #include<bits/stdc++.h>
// using namespace std;

// int main(){
//     int n;
//     cin>>n;
//     int factorial = 1;
//     while(n>0){
//         factorial *=n;
//         n--;
//     }
//     cout<<factorial;
// }


//recursive way
#include<bits/stdc++.h>
using namespace std;
int factorial(int n){
    if(n==0) return 1;

    return n*factorial(n-1);
}

int main(){
    int n;
    cin>>n;
    cout<<factorial(n);
}