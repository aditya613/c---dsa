
#include <iostream>
#include <string>
using namespace std;

class Student {
protected:
    int rollNumber;
    string name;

public:
    Student(int r, string n) {
        rollNumber = r;
        name = n;
        cout << "Student constructor called" << endl;
    }

    ~Student() {
        cout << "Student destructor called" << endl;
    }
};

class Examination : public Student {
protected:
    float marks[5];

public:
    Examination(int r, string n, float m[])
        : Student(r, n) {
        for (int i = 0; i < 5; i++) {
            marks[i] = m[i];
        }
        cout << "Examination constructor called" << endl;
    }

    ~Examination() {
        cout << "Examination destructor called" << endl;
    }
};

class Result : public Examination {
private:
    float total;
    float percentage;
    char grade;

public:
    Result(int r, string n, float m[])
        : Examination(r, n, m) {
        total = 0;

        for (int i = 0; i < 5; i++) {
            total += marks[i];
        }

        percentage = total / 5;

        if (percentage >= 90)
            grade = 'A';
        else if (percentage >= 75)
            grade = 'B';
        else if (percentage >= 60)
            grade = 'C';
        else if (percentage >= 40)
            grade = 'D';
        else
            grade = 'F';

        cout << "Result constructor called" << endl;
    }

    void display() {
        cout << "\nRoll Number: " << rollNumber << endl;
        cout << "Name: " << name << endl;

        for (int i = 0; i < 5; i++) {
            cout << "Subject " << i + 1 << ": " << marks[i] << endl;
        }

        cout << "Total: " << total << "/500" << endl;
        cout << "Percentage: " << percentage << "%" << endl;
        cout << "Grade: " << grade << endl;
    }

    ~Result() {
        cout << "Result destructor called" << endl;
    }
};

int main() {
    float marks[5] = {95, 88, 91, 84, 92};

    {
        Result r(101, "Aditya Gupta", marks);
        r.display();
    }

    return 0;
}
