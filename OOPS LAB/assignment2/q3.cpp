#include<bits/stdc++.h>
using namespace std;

class mathsFun{
    public:

    int factorial(int n){
        int temp = 1;
        for(int i=1;i<=n;i++){
            temp*=i;
        }
        return temp;
    }

    bool primeCheck(int n){
        if (n <= 1) return false;
        for(int i=2;i*i<=n;i++){
            if(n%i==0){
                return false;
            }
        }

        return true;
    }

    bool is_palindrome(int n){
        int original = n;
        int temp = 0;

        while(n > 0){
            temp = (temp * 10) + (n % 10);
            n /= 10;
        }

        if(temp==original){
            return true;
        }
        else{
            return false;
        }
        
    }

    bool is_armstrong(int n){
        int original = n;
        long long temp = 0;

        while(n > 0){
            int digit = n % 10;
            temp += (long long)digit * digit * digit;
            n /= 10;
        }

        if(temp==original){
            return true;
        }
        else{
            return false;
        }
    }

    int calcGCD(int n1, int n2){
        while (n2 != 0) {
        int temp = n2;
        n2 = n1 % n2;
        n1 = temp; 
    }
    return n1;

    }

    int calcLCM(int n1, int n2){
        if (n1 == 0 || n2 == 0) return 0;

        return (n1 / calcGCD(n1, n2)) * n2; 

    }

    pair<int, int> sumAndCountPrime(int L, int R){
        int sum=0;
        int count=0;

        for(int i=L;i<=R;i++){
            if(primeCheck(i)){
                count++;
                sum+=i;
            }
        }

        return {sum,count};
    }


     void fibonacciSeries(int n){
        if(n <= 0) return;
        
        int first = 0, second = 1, sum = 0;
        
        for(int i = 1; i <= n; i++){
            cout << first << " ";
            sum += first;
            
            int next = first + second;
            first = second;
            second = next;
        }
        cout << "\nSum of series: " << sum << endl;
    }

    bool is_strong(int n){
        int original = n;
        int temp = 0;
        
        while(n > 0){
            int digit = n % 10;
            temp += factorial(digit);
            n /= 10;
        }
        
        if(temp == original){
            return true;
        }
        else{
            return false;
        }
    }

};
int main(){


    cout<<"MENU FOR MATHEMATICALS FUNCTIONS;"<<endl;

    cout<<"Below is the menu to perform mathematical functions: Just select number to perform operation"<<endl;
    cout<<"1. Factorial of a number"<<endl;
    cout<<"2. Prime Number Check"<<endl;
    cout<<"3. Reverse & Palindrome Check"<<endl;
    cout<<"4. ArmStrong Number Check"<<endl;
    cout<<"5. GCD of two numbers"<<endl;
    cout<<"6. LCM of two numbers"<<endl;
    cout<<"7. Sum & Count of prime numbers in range"<<endl;
    cout<<"8. Fibonacci Series"<<endl;
    cout<<"9. Strong Number check"<<endl;
    cout<<"10. EXIT"<<endl<<endl;

    mathsFun m1;

    while(true){
        cout<<"Enter num to perform operation: ";
        int x;
        cin>>x;
        cout<<endl;

        switch(x){
           case 1: {
                cout<<"Enter Num to calculate factorial: ";
                int n;
                cin>>n;
                cout<<"Factorial: "<<m1.factorial(n)<<endl<<endl;
                break;
            }
            case 2: {
                cout<<"Enter Num to check prime: ";
                int n;
                cin>>n;
                if(m1.primeCheck(n)){
                    cout<<n<<" is a prime number."<<endl<<endl;
                } else {
                    cout<<n<<" is not a prime number."<<endl<<endl;
                }
                break;
            }
            case 3: {
                cout<<"Enter Num to check palindrome: ";
                int n;
                cin>>n;
                if(m1.is_palindrome(n)){
                    cout<<n<<" is a palindrome number."<<endl<<endl;
                } else {
                    cout<<n<<" is not a palindrome number."<<endl<<endl;
                }
                break;
            }
            case 4: {
                cout<<"Enter Num to check Armstrong: ";
                int n;
                cin>>n;
                if(m1.is_armstrong(n)){
                    cout<<n<<" is an Armstrong number."<<endl<<endl;
                } else {
                    cout<<n<<" is not an Armstrong number."<<endl<<endl;
                }
                break;
            }
            case 5: {
                cout<<"Enter two numbers for GCD: ";
                int n1, n2;
                cin>>n1>>n2;
                cout<<"GCD: "<<m1.calcGCD(n1, n2)<<endl<<endl;
                break;
            }
            case 6: {
                cout<<"Enter two numbers for LCM: ";
                int n1, n2;
                cin>>n1>>n2;
                cout<<"LCM: "<<m1.calcLCM(n1, n2)<<endl<<endl;
                break;
            }
            case 7: {
                cout<<"Enter range (L and R): ";
                int L, R;
                cin>>L>>R;
                pair<int, int> result = m1.sumAndCountPrime(L, R);
                cout<<"Count of primes: "<<result.second<<endl;
                cout<<"Sum of primes: "<<result.first<<endl<<endl;
                break;
            }
            case 8: {
                cout<<"Enter number of terms for Fibonacci: ";
                int n;
                cin>>n;
                m1.fibonacciSeries(n);
                cout<<endl;
                break;
            }
            case 9: {
                cout<<"Enter Num to check Strong: ";
                int n;
                cin>>n;
                if(m1.is_strong(n)){
                    cout<<n<<" is a Strong number."<<endl<<endl;
                } else {
                    cout<<n<<" is not a Strong number."<<endl<<endl;
                }
                break;
            }
            case 10: {
                cout<<"Exiting program..."<<endl;
                return 0;
            }
            default: {
                cout<<"Invalid choice! Please select between 1 and 10."<<endl<<endl;
                break;
            }

        }
    }




}
