#include<bits/stdc++.h>
using namespace std;
class Student{
    public:
    string student_name;
    long long roll_number;
    string branch;
    vector<int> marks;

    int total_marks(){
        int sum=0;
        for(auto i:marks){
            sum+=i;
        }
        return sum;
    } 

    float percentage(){
        float sum=0;
        for(auto i:marks){
            sum+=i;
        }
        return ((sum/500)*100);
    } 

    int average_marks(){
        int sum=0;
        for(auto i:marks){
            sum+=i;
        }
        return (sum/5);
    } 

    int highest_marks(){
        int maxi=0;
        for(auto i:marks){
            maxi = max(i,maxi);
        }
        return maxi;
    } 

    int lowest_marks(){
        int mini=100;
        for(auto i:marks){
            mini=min(mini,i);
        }
        return mini;
    } 
};

int main(){

    Student s1;

    cout<<"Enter Student Name: ";
    cin>>s1.student_name;
    
    cout<<"Enter Roll Number: ";
    cin>>s1.roll_number;

    cout<<"Enter Branch: ";
    cin>>s1.branch;

    for(int i=1;i<=5;i++){
    int temp;
        cout<<"Enter Marks in Subject "<<i<<": ";
    cin>>temp;
    s1.marks.push_back(temp);
    }


    cout<<endl<<"------REPORT CARD--------";
    cout<<endl<<"Student Name: "<<s1.student_name;
    cout<<endl<<"Roll Number: "<<s1.roll_number<<endl;

    cout<<endl<<"Total Marks: "<<s1.total_marks();
    cout<<endl<<"Percentage: "<<s1.percentage()<<"%";
    cout<<endl<<"Average Marks: "<<s1.average_marks();
    cout<<endl<<"Highest Marks: "<<s1.highest_marks();
    cout<<endl<<"Lowest Marks: "<<s1.lowest_marks();

    return 0;


}