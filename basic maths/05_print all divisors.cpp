// Input: N = 36
// Output: [1, 2, 3, 4, 6, 9, 12, 18, 36]  
// Explanation: The divisors of 36 are 1, 2, 3, 4, 6, 9, 12, 18, 36.
// Input: N = 12
// Output: [1, 2, 3, 4, 6, 12]
// Explanation: The divisors of 12 are 1, 2, 3, 4, 6, 12.

//brute force approach - O(n)
#include<bits/stdc++.h>
using namespace std;

vector<int> divisors(int n);

int main(){
    int n;
    cin >> n;
    vector<int> divisor_list = divisors(n);

    for(int i = 0; i < divisor_list.size(); i++){
        cout << divisor_list[i];
        if(i != divisor_list.size() - 1) cout << ", ";
    }
    return 0;
}

vector<int> divisors(int n){
    if(n <= 0) return {};

    vector<int> divisors_list;

    for(int i = 1; i <= n; i++){
        if(n % i == 0){
            divisors_list.emplace_back(i);
        }
    }

    return divisors_list;
}


//better approach - O(sqrt(n))

#include<bits/stdc++.h>
using namespace std;

vector<int> get_divisors(int n);
int main(){
    int n;
    cin>>n;
    vector<int> divisors_list = get_divisors(n);


    //sorting takes O(n log n) here n is number of factors 
    sort(divisors_list.begin(), divisors_list.end());

    //printing takes O(n) n here is number of divisors
    for(auto i:divisors_list){
        cout<<i<<", ";
    }

    return 0;
}

vector<int> get_divisors(int n){
    
    vector<int> nums;
    for(int i=1;i<=sqrt(n);i++){
        if(n%i==0){
            nums.emplace_back(i);
            nums.emplace_back(n/i);
        }
    }

    return nums;
}

//this prints not in ascending order it prints like 1, 36, 2, 18 etc 
// WE CAN FIX THIS By USING SET instead of vector OR sort the vector 

//also for optimization instead of using 'sqrt' method we can use n*n for more efficient time management