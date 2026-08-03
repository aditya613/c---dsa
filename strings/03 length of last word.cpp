#include<bits/stdc++.h>
using namespace std;

int main(){
    string s;

    getline(cin,s);
    
        int i = s.size() - 1;

        while (i >= 0 && s[i] == ' ')
            i--;

        int count = 0;

        while (i >= 0 && s[i] != ' ') {
            count++;
            i--;
        }

        return count;
}