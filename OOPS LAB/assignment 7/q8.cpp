#include <bits/stdc++.h>
using namespace std;

class Student {
public:
    int rollNo;
    string name;
    float m1, m2, m3;

    void input() {
        cout << "Enter roll number: ";
        cin >> rollNo;

        cout << "Enter name: ";
        cin >> name;

        cout << "Enter marks in three subjects: ";
        cin >> m1 >> m2 >> m3;
    }

    float total() {
        return m1 + m2 + m3;
    }

    float percentage() {
        return total() / 3.0;
    }

    void display() {
        cout << "\nRoll No: " << rollNo << endl;
        cout << "Name: " << name << endl;
        cout << "Marks: " << m1 << " " << m2 << " " << m3 << endl;
        cout << "Total: " << total() << endl;
        cout << "Percentage: " << percentage() << "%" << endl;
    }
};

int main() {
    int n;

    cout << "Enter number of students: ";
    cin >> n;

    Student **s = new Student*[n];

    for (int i = 0; i < n; i++) {
        s[i] = new Student;
        cout << "\nEnter details of student " << i + 1 << endl;
        s[i]->input();
    }

    int highest = 0;

    cout << "\nStudent Results" << endl;

    for (int i = 0; i < n; i++) {
        s[i]->display();

        if (s[i]->percentage() > s[highest]->percentage()) {
            highest = i;
        }
    }

    cout << "\nStudent with Highest Percentage" << endl;
    s[highest]->display();

    for (int i = 0; i < n; i++) {
        delete s[i];
    }

    delete[] s;

    return 0;
}