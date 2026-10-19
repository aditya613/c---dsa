#include <bits/stdc++.h>
using namespace std;

class UniversityManagement {
private:
    const long long studentID;
    static string universityName ;
    static constexpr int maxCredits = 30;

public:
    UniversityManagement(long long id) : studentID(id) {}

    constexpr static int calculateRemainingCredits(int usedCredits) {
        return maxCredits - usedCredits;
    }

    void display(int usedCredits) {
        cout << "Student ID: " << studentID << endl;
        cout << "University: " << universityName << endl;
        cout << "Maximum Credits: " << maxCredits << endl;
        cout << "Used Credits: " << usedCredits << endl;
        cout << "Remaining Credits: " << calculateRemainingCredits(usedCredits) << endl;
    }

    static void changeUniversityName(string name) {
        universityName = name;
    }
};

string UniversityManagement :: universityName = "PEC UNIVERSITY OF TECHNOLOGY" ;

int main() {
    UniversityManagement s1(101);
    UniversityManagement s2(102);
    s1.display(20);
    s2.display(25);
    s1.changeUniversityName("IIT Delhi"); 
    cout << "After changing university name:" << endl << endl;
    s1.display(20);
    s2.display(25);

    return 0;
}