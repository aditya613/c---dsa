#include <bits/stdc++.h>
using namespace std;

class Employee {
public:
    int empID;

protected:
    string name;

private:
    double salary;

public:
    Employee(int id, string n, double s) {
        empID = id;
        name = n;
        salary = s;
    }

    void display() {
        cout << "Employee ID: " << empID << endl;
        cout << "Name: " << name << endl;
        cout << "Salary: " << salary << endl;
    }
};

class PublicManager : public Employee {
public:
    string department;

    PublicManager(int id, string n, double s, string d) : Employee(id, n, s) {
        department = d;
    }

    void displayDetails() {
        cout << "\nPublic Inheritance" << endl;
        cout << "Employee ID: " << empID << endl;
        cout << "Name: " << name << endl;
        display();
        cout << "Department: " << department << endl;
    }
};

class PrivateManager : private Employee {
public:
    string department;

    PrivateManager(int id, string n, double s, string d) : Employee(id, n, s) {
        department = d;
    }

    void displayDetails() {
        cout << "\nPrivate Inheritance" << endl;
        cout << "Employee ID: " << empID << endl;
        cout << "Name: " << name << endl;
        display();
        cout << "Department: " << department << endl;
    }
};

class ProtectedManager : protected Employee {
public:
    string department;

    ProtectedManager(int id, string n, double s, string d) : Employee(id, n, s) {
        department = d;
    }

    void displayDetails() {
        cout << "\nProtected Inheritance" << endl;
        cout << "Employee ID: " << empID << endl;
        cout << "Name: " << name << endl;
        display();
        cout << "Department: " << department << endl;
    }
};

int main() {
    PublicManager m1(101, "Rahul", 50000, "IT");
    PrivateManager m2(102, "Aman", 60000, "HR");
    ProtectedManager m3(103, "Rohit", 70000, "Finance");

    m1.displayDetails();
    m2.displayDetails();
    m3.displayDetails();

    cout << "\nAccessing members outside classes:" << endl;

    cout << "Public Manager ID: " << m1.empID << endl;
    cout << "Public Manager Department: " << m1.department << endl;

    cout << "Private Manager Department: " << m2.department << endl;

    cout << "Protected Manager Department: " << m3.department << endl;

    return 0;
}