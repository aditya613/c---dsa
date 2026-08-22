#include<bits/stdc++.h>
using namespace std;

class student{
    public:

    string calcGrade(int marks){
        if(marks>=90){
            return "A+";
        }
        
        else if(marks>=80){
            return "A";
        }
        else if(marks>=70){
            return "B";
        }
        else if(marks>=60){
            return "C";
        }
        else if(marks>=50){
            return "D";
        }
        else{
            return "F";
        }
    }

    bool isFail(int marks){
        return (marks<50)?true:false;
    }
};
int main(){

    student s1;
    for(int i=1;i<=5;i++){
        cout<<"Enter Marks of "<<i<<" Subject: ";
        int temp;
        cin>>temp;
        cout<<"Grade of Student: "<<s1.calcGrade(temp)<<endl;
        if(s1.isFail(temp)){
            cout<<"Student is Fail! Better Luck next time."<<endl;
        }
    }

    return 0;



}