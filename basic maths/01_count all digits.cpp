// Example 1:
// Input:N = 12345
// Output:5
// Explanation:  The number 12345 has 5 digits.
                        
// Example 2:
// Input:N = 7789              
// Output: 4
// Explanation: The number 7789 has 4 digits.  

#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;

    int digits = 0;
    while (n > 0) {
        digits += 1;
        n = n / 10;
    }

    cout << digits;
    return 0;
}


//N%10 returns last digit
//N/10 (int) removes the one's digit from number every time
