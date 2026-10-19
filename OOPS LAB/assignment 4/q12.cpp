#include <bits/stdc++.h>
using namespace std ; 

class Account{
private:
    int accNumber ; 
    double balance ; 
public: 
    Account(int num , double bal){
        accNumber = num ; 
        balance = bal;
    }
    void transfer(Account * acc1 ,Account *acc2 , double amount){
        if(acc1 == NULL || acc2 == NULL || acc1 -> balance < amount){
            cout << "INVALID TRANSACTION " << endl;
            return ;
        }
        acc1 -> balance -= amount ; 
        acc2 -> balance += amount ;
    }
    void diplay(){
        cout << "ACCOUNT NUMBER = " << accNumber << endl;
        cout << "ACCOUNT BALANCE = " << balance << endl; 
        cout << "--------------------------" << endl;
    }
}; 

int main(){
    Account acc1(125 , 5000);
    Account acc2(250 , 4500);
    acc1.diplay();
    acc2.diplay();
    acc1.transfer(&acc1 , &acc2 ,2500);
    acc1.diplay();
    acc2.diplay();

    return 0;
}