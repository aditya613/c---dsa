#include <bits/stdc++.h>
using namespace std;

class Student {
public:
    int rollNo;

protected:
    string name;

private:
    float marks;

public:
    Student(int r, string n, float m) {
        rollNo = r;
        name = n;
        marks = m;
    }

    float getMarks() {
        return marks;
    }
};

class PublicResult : public Student {
public:
    PublicResult(int r, string n, float m) : Student(r, n, m) {}

    void display() {
        cout << "\nPublic Inheritance" << endl;
        cout << "Roll No: " << rollNo << endl;
        cout << "Name: " << name << endl;
        cout << "Percentage: " << getMarks() << "%" << endl;
    }
};

class PrivateResult : private Student {
public:
    PrivateResult(int r, string n, float m) : Student(r, n, m) {}

    void display() {
        cout << "\nPrivate Inheritance" << endl;
        cout << "Roll No: " << rollNo << endl;
        cout << "Name: " << name << endl;
        cout << "Percentage: " << getMarks() << "%" << endl;
    }
};

class ProtectedResult : protected Student {
public:
    ProtectedResult(int r, string n, float m) : Student(r, n, m) {}

    void display() {
        cout << "\nProtected Inheritance" << endl;
        cout << "Roll No: " << rollNo << endl;
        cout << "Name: " << name << endl;
        cout << "Percentage: " << getMarks() << "%" << endl;
    }
};

int main() {
    PublicResult s1(101, "Rahul", 85);
    PrivateResult s2(102, "Aman", 90);
    ProtectedResult s3(103, "Rohit", 78);

    s1.display();
    s2.display();
    s3.display();

    cout << "\nAccessing members outside classes:" << endl;

    cout << "Public Roll No: " << s1.rollNo << endl;

    cout << "Private and Protected objects cannot access rollNo directly." << endl;

    return 0;
}