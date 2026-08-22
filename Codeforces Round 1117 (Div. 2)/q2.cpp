#include <bits/stdc++.h>
using namespace std;

int main() {
    int t;
    cin >> t;

   while (t--) {
        int n, m;
        cin >> n >> m;

        long long a1, b1;

        cin >> a1;
        for (int i = 1; i < n; i++) {
            long long x;
            cin >> x;
        }

        cin >> b1;
        for (int i = 1; i < m; i++) {
            long long x;
            cin >> x;
        }

        long long beaSurvival = a1 + n - 1;
        long long verSurvival = b1 + m - 1;

        if (verSurvival <= beaSurvival)
            cout << 1 << '\n';
        else
            cout << 2 << '\n';
    }

    return 0;
}