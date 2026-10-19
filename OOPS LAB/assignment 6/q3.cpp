
#include <iostream>
#include <string>
using namespace std;

class Student {
protected:
    int rollNumber;
    string studentName;

public:
    Student(int r, string n) {
        rollNumber = r;
        studentName = n;
    }

    void display() {
        cout << "Roll Number: " << rollNumber << endl;
        cout << "Student Name: " << studentName << endl;
    }
};

class Employee {
protected:
    int employeeID;
    string employeeName;

public:
    Employee(int id, string n) {
        employeeID = id;
        employeeName = n;
    }

    void display() {
        cout << "Employee ID: " << employeeID << endl;
        cout << "Employee Name: " << employeeName << endl;
    }
};

class TeachingAssistant : public Student, public Employee {
public:
    TeachingAssistant(int r, string sn, int id, string en)
        : Student(r, sn), Employee(id, en) {}
};

int main() {
    TeachingAssistant t(101, "Aditya Gupta", 501, "ABCD");

    t.Student::display();
    t.Employee::display();

    return 0;
}
