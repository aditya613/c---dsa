#include <bits/stdc++.h>
using namespace std;

int main() {

    int t;
    cin >> t;

    while (t--) {

        int n, m;
        cin >> n >> m;

        unordered_set<char> availableChars;

        // Store first character of every ordinary word
        for (int i = 0; i < n; i++) {
            string temp;
            cin >> temp;

            availableChars.insert(temp[0]);
        }

        bool possible = true;

        // Check every abbreviation
        for (int i = 0; i < m; i++) {

            string temp;
            cin >> temp;

            for (char c : temp) {

                char lowercase = tolower(c);

                if (availableChars.find(lowercase) == availableChars.end()) {
                    possible = false;
                }
            }
        }

        if (possible) {
            cout << "YES\n";
        }
        else {
            cout << "NO\n";
        }
    }

    return 0;
}