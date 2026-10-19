#include <bits/stdc++.h> 
using namespace std ; 

class Course{
private :
    const long long courseCode ; 
    static string uniName ; 
    static int count ; 
    int courseCredits ;
    constexpr static int maxAllowedCredit = 5; 
public : 
    Course(long long coursecode , int credits) : courseCode(coursecode){
        if(credits > maxAllowedCredit){
            courseCredits = maxAllowedCredit ;
        }else{
            courseCredits = credits ;
        }

        count ++ ;
    }; 

    void display(){
        cout << "Course Code :- " << courseCode << endl; 
        cout << "University Name :- " << uniName << endl; 
        cout << "Total courses :- " << count << endl; 
        cout << "Course Creadits :- " << courseCredits << endl;
        cout << "-----------------------------" << endl;
    }



};
string Course :: uniName = "PEC UNIVERSIY OF TECHNOLOGY ";
int Course :: count = 0 ;

int main(){
    Course c1(25103028 , 4);
    c1.display();
    Course c2(23453245 , 6);
    c2.display();

    return 0 ;
}