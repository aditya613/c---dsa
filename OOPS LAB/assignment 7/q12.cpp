#include <bits/stdc++.h>
using namespace std;

class Payment {
public:
    virtual void processPayment() = 0;
};

class CreditCardPayment : public Payment {
public:
    string cardNumber;
    float amount;

    void processPayment() override {
        cout << "Enter card number: ";
        cin >> cardNumber;

        cout << "Enter amount: ";
        cin >> amount;

        cout << "Credit Card Payment Successful: " << amount << endl;
    }
};

class UPIPayment : public Payment {
public:
    string upiID;
    float amount;

    void processPayment() override {
        cout << "Enter UPI ID: ";
        cin >> upiID;

        cout << "Enter amount: ";
        cin >> amount;

        cout << "UPI Payment Successful: " << amount << endl;
    }
};

class CashPayment : public Payment {
public:
    float amount;

    void processPayment() override {
        cout << "Enter cash amount: ";
        cin >> amount;

        cout << "Cash Payment Successful: " << amount << endl;
    }
};

int main() {
    CreditCardPayment c;
    UPIPayment u;
    CashPayment cash;

    Payment *ptr[3];

    ptr[0] = &c;
    ptr[1] = &u;
    ptr[2] = &cash;

    for (int i = 0; i < 3; i++) {
        ptr[i]->processPayment();
        cout << endl;
    }

    return 0;
}