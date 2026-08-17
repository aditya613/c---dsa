#include<bits/stdc++.h>
using namespace std;

bool is_palin(string s){


    if(s.length()<=1){
        return true;
    }

    if(s[0] == s[s.size()-1]) return is_palin(s.substr(1, s.size()-2));
    else return false;

}


int main(){

    string s;
    cout<<"Enter a string: ";
    cin>>s;

     string clean = "";

    for (char c : s) {
        if (isalnum(c)) {
            clean += tolower(c);
        }
    }


    if(is_palin(clean)){
    cout<<s<<" is a palindrone";
    }
    else{
        cout<<s<<" is not a palind";
    }
}