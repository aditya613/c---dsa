#include <bits/stdc++.h>
using namespace std ; 

class BankAccount{
    const long long accNumber ;
    double amount ; 
public:
    BankAccount(int AccNumber , int Amount) : accNumber(AccNumber){
        amount = Amount ;
    }

    void deposit(int val){
        amount += val;
    }

    void withdraw(int val){
        if(val > amount){
            cout << "INVALID INPUT" << endl;
        }else{
            amount -= val;
        }
    }

    void diplay(){
        cout << "ACCOUNT NUMBER = " << accNumber << endl;
        cout << "ACCOUNT BALANCE = " << amount << endl;
    }
};
int main(){
    BankAccount acc1(34 , 450000) ;
    acc1.withdraw(5000);
    acc1.deposit(3500);
    acc1.diplay();
    return 0;
}