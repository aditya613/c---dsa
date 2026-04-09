// #find gcd/hcf  of two  numbers
// Example 1:
// Input: N1 = 9, N2 = 12

// Output: 3
// Explanation:
// Factors of 9: 1, 3, 9
// Factors of 12: 1, 2, 3, 4, 6, 12
// Common Factors: 1, 3
// Greatest common factor: 3 (GCD)

// Example 2:
// Input: N1 = 20, N2 = 15

// Output: 5
// Explanation:
// Factors of 20: 1, 2, 4, 5, 10, 20
// Factors of 15: 1, 3, 5, 15
// Common Factors: 1, 5
// Greatest common factor: 5 (GCD)
    

//option1 brute force approach

#include<bits/stdc++.h>
using namespace std;
int find_gcd(int n1, int n2);
int main(){

    int n1,n2;
    cin>>n1>>n2;
    cout<<find_gcd(n1,n2);

}

int find_gcd(int n1, int n2){

    int gcd = 1;
    for(int i=1; i<=min(n1,n2); i++){
        if(n1%i==0 && n2%i==0){
            gcd = i;
        }
    }

    return gcd;

}

//time complexity of above is O(min(n1,n2))     i.e linear T.C


//option 2 better approach but still O(min(n1,n2)) for worst case
// here instead of running the loop till end we stop the loop as soon as we find the gcd
// we iterate descendingly to find max gcd value

#include<bits/stdc++.h>
using namespace std;
int find_gcd(int n1, int n2);
int main(){

    int n1,n2;
    cin>>n1>>n2;
    cout<<find_gcd(n1,n2);
    return 0;
}
int find_gcd(int n1, int n2){
    
    for(int i=min(n1,n2); i>=1; i--){
        if(n1%i==0 && n2%i==0){
            return i;
        }
    }
}



//now comes option3 a little better optimised approach. 
// we use euclidean algorithm which states that gcd(n1,n2)=gcd(n1-n2, n2) [n1>n2] 
// we keep on doing this subtraction till one number becomes 0 and the other number will be gcd of the original question

// T.C still O(n) linear here but we use this concept in option4 for best outcome
#include<bits/stdc++.h>
using namespace std;
int euclidean_gcd(int n1, int n2);
int main(){
    int n1,n2;
    cin>>n1>>n2;

    cout<<euclidean_gcd(n1,n2);
}

int euclidean_gcd(int n1, int n2){
    
    while(n1>0 && n2>0){

        if(n1>n2) n1-=n2;
        else n2-=n1;

    }

    if(n1==0) return n2;
    else return n1;
    
}


//bestest and most optimised solution is that gcd(n1,n2) = gcd(n1%n2, n2) [n1>n2]
// this is similar to above solution but even better with less time complexity
// O(log fi (min(n1,n2))
#include<bits/stdc++.h>
using namespace std;
int euclidean_gcd(int n1, int n2);
int main(){
    int n1,n2;
    cin>>n1>>n2;

    cout<<euclidean_gcd(n1,n2);
}

int euclidean_gcd(int n1, int n2){
    
    while(n1>0 && n2>0){

        if(n1>n2) n1%=n2;
        else n2%=n1;

    }

    if(n1==0) return n2;
    else return n1;
    
}