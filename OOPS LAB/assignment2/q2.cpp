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
        int temp = 0;
        for(auto i:nums){
            if(i<0){
                temp++;
            }
        }
        return temp; 
    }

    int numZeros(){
        int temp = 0;
        for(auto i:nums){
            if(i==0){
                temp++;
            }
        }
        return temp;
    }

    int sumPositiveNums(){
         int temp = 0;
        for(auto i:nums){
            if(i>0){
                temp+=i;
            }
        }
        return temp;
    }


    int sumNegativeNums(){
        int temp = 0;
        for(auto i:nums){
            if(i<0){
                temp+=i;
            }
        }
        return temp; 
    }

};
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

    cout<<"Number of positive numbers: "<<s1.positiveNums()<<endl;
    cout<<"Number of negative numbers: "<<s1.negativeNums()<<endl;

    cout<<"Number of Zeros: "<<s1.numZeros()<<endl;

    cout<<"Sum of positive numbers: "<<s1.sumPositiveNums()<<endl;
    cout<<"Sum of negative numbers: "<<s1.sumNegativeNums()<<endl;



}