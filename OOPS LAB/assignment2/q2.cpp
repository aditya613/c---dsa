#include<bits/stdc++.h>
using namespace std;
class student{
    public:
    vector<int> nums;

    void insertNum(int num){
        nums.push_back(num);
    }

    int positiveNums(){
        int temp = 0;
        for(auto i:nums){
            if(i>0){
                temp++;
            }
        }
        return temp;
    }

    int negativeNums(){
        int 
    }
}
int main(){

    int N;
    cout<<"Enter N: ";
    cin>>N;

    student s1;
    
    for(int i=0;i<N;i++){
        int temp;
        cin>>temp;
        s1.insertNum(temp);
    }


}