#include <bits/stdc++.h>
using namespace std;

class Employee {
public:
    virtual void calculateSalary() {
        cout << "Calculating salary" << endl;
    }
};

class PermanentEmployee : public Employee {
public:
    float basic, allowances;

    PermanentEmployee(float b, float a) {
        basic = b;
        allowances = a;
    }

    void calculateSalary() override {
        cout << "Permanent Employee Salary: " << basic + allowances << endl;
    }
};

class ContractEmployee : public Employee {
public:
    int hours;
    float rate;

    ContractEmployee(int h, float r) {
        hours = h;
        rate = r;
    }

    void calculateSalary() override {
        cout << "Contract Employee Salary: " << hours * rate << endl;
    }
};

int main() {
    PermanentEmployee p(30000, 10000);
    ContractEmployee c(160, 200);

    Employee *ptr;

    ptr = &p;
    ptr->calculateSalary();

    ptr = &c;
    ptr->calculateSalary();

    return 0;
}