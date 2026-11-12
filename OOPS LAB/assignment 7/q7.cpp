#include <bits/stdc++.h>
using namespace std;

class BankAccount {
public:
    int accNo;
    string name;
    float balance;

    void deposit(float amount) {
        balance += amount;
        cout << "Amount deposited: " << amount << endl;
    }

    void withdraw(float amount) {
        if (amount <= balance) {
            balance -= amount;
            cout << "Amount withdrawn: " << amount << endl;
        }
        else {
            cout << "Insufficient balance" << endl;
        }
    }

    void display() {
        cout << "\nAccount Number: " << accNo << endl;
        cout << "Account Holder: " << name << endl;
        cout << "Balance: " << balance << endl;
    }
};

int main() {
    BankAccount *ptr = new BankAccount;

    ptr->accNo = 101;
    ptr->name = "Rahul";
    ptr->balance = 5000;

    ptr->deposit(2000);
    ptr->withdraw(1500);

    ptr->display();

    delete ptr;

    return 0;
}