class test{
public:
    bool isPrime(int n){
        for(int i = 2 ; i*i <= n ;i++){
            if(n % i == 0){
                return false ;
            }
        }
        return true ;
    }

    int fact(int n){
        if( n == 0 || n == 1){
            return 1 ;
        }

        return n * fact(n-1);
    }

    int GCD(int a , int b){
        while(b != 0){
            int temp = b ;
            b = a % b ; 
            a = temp;
        }
        return a ;
    }

    int power(int a , int b){
        if(a == 1){
            return 1 ;
        }
        if(b == 0){
            return 1 ;
        }

        int ans = power(a , b/2);
        if(b % 2 == 0){
            return ans * ans ;
        }else{
            return a * ans * ans ;
        }
    }
};