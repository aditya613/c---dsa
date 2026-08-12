#include<bits/stdc++.h>
using namespace std;
int main(){
    int n;

    cout << "Enter an integer: ";
    cin >> n;

    if (n & 1)
        cout << "The number is Odd";
    else
        cout << "The number is Even";

    return 0;
}