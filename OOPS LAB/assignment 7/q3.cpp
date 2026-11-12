#include <bits/stdc++.h>
using namespace std;

class Student {
public:
    int rollNo;
    string name;

    Student(int r, string n) {
        rollNo = r;
        name = n;
        cout << "Base class constructor called" << endl;
    }
};

class Result : public Student {
public:
    int m1, m2, m3;

    Result(int r, string n, int a, int b, int c) : Student(r, n) {
        m1 = a;
        m2 = b;
        m3 = c;
        cout << "Derived class constructor called" << endl;
    }

    void display() {
        int total = m1 + m2 + m3;
        float percentage = total / 3.0;

        cout << "\nRoll No: " << rollNo << endl;
        cout << "Name: " << name << endl;
        cout << "Total Marks: " << total << endl;
        cout << "Percentage: " << percentage << "%" << endl;
    }
};

int main() {
    Result s(101, "Rahul", 85, 90, 80);

    s.display();

    return 0;
}