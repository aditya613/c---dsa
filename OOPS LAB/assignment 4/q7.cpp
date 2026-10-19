#include <bits/stdc++.h>
using namespace std ; 

class SmartMeter{
private:
    const long long meterID; 
    int units ;
    static double rate ; 
    constexpr static int maxUnits = 500;
    constexpr static int penalty = 500 ;
public : 
    SmartMeter(long long mtrID , int unit) : meterID(mtrID){
        units = unit ;
    };

    void display(){
        cout << "METER ID = " << meterID << endl; 
        cout << "BILL FOR THE MONTH = Rs." << bill() << endl;
        if(units >= maxUnits){
            cout << "YOU HAVE BEEN FINNED FOR EXCEEDING MAXLIMIT OF UNITS PER MONTH" << endl;
        }
    }

    double bill(){
        double amount = 0 ;
        if(units < maxUnits){
            amount += units * rate ;
        }else{
            amount = amount + units * rate + penalty ;
        }
        return amount ;
    }
}; 

double SmartMeter :: rate = 7.5 ;
int main(){
    SmartMeter m1(2112 , 200);
    m1.display();
    return 0;
}
