#include<bits/stdc++.h>
using namespace std;

int main()
{
    int a, b, c, d;
    int e, f, g, h;

    cout << "Enter value of a : ";
    cin >> a;

    cout << "Enter value of b : ";
    cin >> b;

    cout << "Enter value of c : ";
    cin >> c;

    cout << "Enter value of d : ";
    cin >> d;

    cout << "Enter value of e : ";
    cin >> e;

    cout << "Enter value of f : ";
    cin >> f;

    cout << "Enter value of g : ";
    cin >> g;

    cout << "Enter value of h : ";
    cin >> h;

    bool result = (a + b * c) > d && (e != f || g <= h);

    cout << endl;
    cout << "Result of Expression : " << result << endl;

    cout << endl;
    cout << "Operator Precedence Used :" << endl;
    cout << "1. *" << endl;
    cout << "2. +" << endl;
    cout << "3. >" << endl;
    cout << "4. !=" << endl;
    cout << "5. <=" << endl;
    cout << "6. ||" << endl;
    cout << "7. &&" << endl;

    return 0;
}