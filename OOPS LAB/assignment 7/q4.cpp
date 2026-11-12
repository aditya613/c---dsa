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

    ~Person() {
        cout << "Person destructor called" << endl;
    }
};

class Employee : public Person {
public:
    int empID;
    string designation;

    Employee(string n, int a, int id, string d) : Person(n, a) {
        empID = id;
        designation = d;
        cout << "Employee constructor called" << endl;
    }

    ~Employee() {
        cout << "Employee destructor called" << endl;
    }
};

class Salary : public Employee {
public:
    float basic, hra, da;

    Salary(string n, int a, int id, string d, float b)
        : Employee(n, a, id, d) {
        basic = b;
        hra = basic * 0.20;
        da = basic * 0.10;
        cout << "Salary constructor called" << endl;
    }

    void display() {
        float gross = basic + hra + da;

        cout << "\nEmployee Details" << endl;
        cout << "Name: " << name << endl;
        cout << "Age: " << age << endl;
        cout << "Employee ID: " << empID << endl;
        cout << "Designation: " << designation << endl;
        cout << "Basic Salary: " << basic << endl;
        cout << "HRA: " << hra << endl;
        cout << "DA: " << da << endl;
        cout << "Gross Salary: " << gross << endl;
    }

    ~Salary() {
        cout << "Salary destructor called" << endl;
    }
};

int main() {
    {
        Salary s("Rahul", 25, 101, "Manager", 50000);
        s.display();
    }

    return 0;
}