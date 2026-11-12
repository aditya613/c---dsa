#include <bits/stdc++.h>
using namespace std;

class Person {
public:
    string name;
    int age;

    Person(string n, int a) {
        name = n;
        age = a;
        cout << "Person constructor called" << endl;
    }

    virtual void displayDetails() {
        cout << "Name: " << name << endl;
        cout << "Age: " << age << endl;
    }
};

class Student : public Person {
public:
    int rollNo;
    string course;

    Student(string n, int a, int r, string c) : Person(n, a) {
        rollNo = r;
        course = c;
        cout << "Student constructor called" << endl;
    }
};

class Examination : public Student {
public:
    int marks[5];

    Examination(string n, int a, int r, string c, int m[])
        : Student(n, a, r, c) {
        for (int i = 0; i < 5; i++) {
            marks[i] = m[i];
        }

        cout << "Examination constructor called" << endl;
    }

    void displayDetails() override {
        int total = 0;

        cout << "\nStudent Details" << endl;
        cout << "Name: " << name << endl;
        cout << "Age: " << age << endl;
        cout << "Roll No: " << rollNo << endl;
        cout << "Course: " << course << endl;

        cout << "Marks: ";

        for (int i = 0; i < 5; i++) {
            cout << marks[i] << " ";
            total += marks[i];
        }

        float percentage = total / 5.0;

        cout << "\nTotal Marks: " << total << endl;
        cout << "Percentage: " << percentage << "%" << endl;
    }
};

int main() {
    int m[5];

    cout << "Enter marks in five subjects: ";

    for (int i = 0; i < 5; i++) {
        cin >> m[i];
    }

    Examination *obj = new Examination("Rahul", 20, 101, "CSE", m);

    Person *ptr = obj;

    ptr->displayDetails();

    delete obj;

    return 0;
}