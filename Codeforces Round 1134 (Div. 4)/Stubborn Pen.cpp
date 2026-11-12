
#include <bits/stdc++.h>
using namespace std;

int main() {
    int t;
    cin >> t;

    while (t--) {
        int n;
        cin >> n;

        string s;
        cin >> s;

        int manualSwitch = 0;
        char curr = 'R';

        for (int i = 0; i < n; i++) {

            if (s[i] != curr) {
                manualSwitch++;
                curr = (curr == 'R' ? 'B' : 'R');
            }

            curr = (curr == 'R' ? 'B' : 'R');
        }

        cout << manualSwitch << '\n';
    }

    return 0;
}
