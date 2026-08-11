#include<bits/stdc++.h>
using namespace std;

class Student{
    public:
    string name;
    long long rollNumber;
    float cgpa;
};

int main(){
    Student s1;
    s1.name = "Aditya";
    s1.rollNumber= 124141;
    s1.cgpa=8.93;

    cout<<s1.name;

    return 0;
}