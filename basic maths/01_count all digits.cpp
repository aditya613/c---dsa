// Example 1:
// Input:N = 12345
// Output:5
// Explanation:  The number 12345 has 5 digits.
                        
// Example 2:
// Input:N = 7789              
// Output: 4
// Explanation: The number 7789 has 4 digits.  

#include<bits/stdc++.h>

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
//this takes 1 loop i.e O(n)

//N%10 returns last digit
//N/10 (int) removes the one's digit from number every time


//more Optimal solution in O(1)
 int main(){
    int n;
    cin>>n;

    int digits = (int) (log10(n)+1);
    cout<<digits;
 }