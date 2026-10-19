#include <bits/stdc++.h>
using namespace std;

class Employee {
private:
    int EmployeeID;
    double basicSalary;
    int rating;
    static constexpr int maxRating = 5;
public:
    Employee(int Id, double salary, int rate) {
        EmployeeID = Id;
        basicSalary = salary;
        if (rating > maxRating) {
            rating = maxRating;
        }else{
            rating = rate;
        }
    }
    void salaryChange(Employee &e1) {
        if (e1.rating == 5) {
            e1.basicSalary *= 1.5;
        }else if (e1.rating > 4) {
            e1.basicSalary *= 1.25;
        }else if (e1.rating > 3) {
            e1.basicSalary *= 1.125;
        }
    }
    void display() {
        cout << "Employee ID = " << EmployeeID << endl;
        cout << "Basic Salary = " << basicSalary << endl;
        cout << "Performance Rating = " << rating << endl;
    }
};
int main() {
    Employee emp1(1, 5000, 4);
    cout << "BEFORE SALARY REVISION" << endl;;
    emp1.display();
    emp1.salaryChange(emp1);
    cout << "AFTER SALARY REVISION" << endl;;
    emp1.display();

    return 0;
}