
#include <iostream>
#include <string>
using namespace std;

class Employee {
protected:
    int employeeID;
    string name;
    double basicSalary;

public:
    Employee(int id, string n, double salary) {
        employeeID = id;
        name = n;
        basicSalary = salary;
    }
};

class Manager : protected Employee {
protected:
    double bonusPercentage;
    double grossSalary;

public:
    Manager(int id, string n, double salary, double bonus)
        : Employee(id, n, salary) {
        bonusPercentage = bonus;
        grossSalary = basicSalary + basicSalary * bonusPercentage / 100;
    }
};

class SeniorManager : public Manager {
public:
    SeniorManager(int id, string n, double salary, double bonus)
        : Manager(id, n, salary, bonus) {}

    void display() {
        cout << "Employee ID: " << employeeID << endl;
        cout << "Name: " << name << endl;
        cout << "Basic Salary: " << basicSalary << endl;
        cout << "Bonus Percentage: " << bonusPercentage << "%" << endl;
        cout << "Gross Salary: " << grossSalary << endl;
    }
};

int main() {
    SeniorManager s(101, "Aditya Gupta", 50000, 20);
    s.display();

    return 0;
}
