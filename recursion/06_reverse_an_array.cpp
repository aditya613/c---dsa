//Problem Statement: You are given an array. The task is to reverse the array and print it.

// Input: N = 5, arr[] = {5,4,3,2,1}
// Output: {1,2,3,4,5}
// Explanation: Since the order of elements gets reversed the first element will occupy the fifth position, the second element occupies the fourth position and so on.

// Input: N=6 arr[] = {10,20,30,40}
// Output: {40,30,20,10}
// Explanation: Since the order of elements gets reversed the first element will occupy the fifth position, the second element occupies the fourth position and so on.

#include<bits/stdc++.h>
using namespace std;
void reverse_array(vector<int> &array, int n){
    int size = array.size();

    if(n >= size/2) {
        for(auto it:array){
            cout<<it;
        }
        return;
    }

    swap(array[n], array[size-n-1]);

    reverse_array(array, n+1);
}

int main(){
    vector<int> ls = {1,2,3,4,5};
    reverse_array(ls, 0);

}