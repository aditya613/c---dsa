#include <bits/stdc++.h>
using namespace std;

int main() {
    char str[100], rev[100];
    char *p = str;

    cout << "Enter a string: ";
    cin.getline(str, 100);

    int len = 0, vowels = 0, consonants = 0;

    while (*(p + len) != '\0') {
        char ch = *(p + len);

        if (ch >= 'A' && ch <= 'Z')
            ch = ch + 32;

        if (ch >= 'a' && ch <= 'z') {
            if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u')
                vowels++;
            else
                consonants++;
        }

        len++;
    }

    cout << "Length: " << len << endl;
    cout << "Vowels: " << vowels << endl;
    cout << "Consonants: " << consonants << endl;

    for (int i = 0; i < len; i++) {
        *(rev + i) = *(p + len - 1 - i);
    }

    rev[len] = '\0';

    cout << "Reversed string: " << rev << endl;

    bool palindrome = true;

    for (int i = 0; i < len / 2; i++) {
        if (*(p + i) != *(p + len - 1 - i)) {
            palindrome = false;
            break;
        }
    }

    if (palindrome)
        cout << "String is a palindrome";
    else
        cout << "String is not a palindrome";

    return 0;
}