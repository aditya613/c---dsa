#include<bits/stdc++.h>
using namespace std;


int main()
{
    int first;
    int second;

    cout << "Enter First Integer : ";
    cin >> first;

    cout << "Enter Second Integer : ";
    cin >> second;

    if (second == 0)
    {
        cout << "Division by zero Error" << endl;
    }
    else
    {
        float result = (float)first / second;

        cout << "Division Result : " << result << endl;
    }

    return 0;
}