#include<iostream>
using namespace std;

bool isPrime(int n){
    if(n<2){
        return false;
    }
    for(int i=2;i*i<=n;i++){
        if(n%i==0){
            return false;
        }
    }
    return true;
}

int countPrime(int* arr,int n,int key){
    int count=0;
    for(int i=0;i<n;i++){
        if(arr[i]==key){
            count++;
        }
    }
    return count;
}

int findPrimes(int* arr,int n,int* primes,int* frequency){
    int primeCount=0;
    for(int i=0;i<n;i++){
        if(isPrime(arr[i])){
            bool found=false;
            for(int j=0;j<primeCount;j++){
                if(primes[j]==arr[i]){
                    found=true;
                    break;
                }
            }
            if(!found){
                primes[primeCount]=arr[i];
                frequency[primeCount]=countPrime(arr,n,arr[i]);
                primeCount++;
            }
        }
    }
    return primeCount;
}

int mostFrequent(int* primes,int* frequency,int primeCount){
    int index=0;
    for(int i=1;i<primeCount;i++){
        if(frequency[i]>frequency[index]){
            index=i;
        }
    }
    return primes[index];
}

void sortByFrequency(int* primes,int* frequency,int primeCount){
    for(int i=0;i<primeCount-1;i++){
        for(int j=0;j<primeCount-i-1;j++){
            if(frequency[j]>frequency[j+1]){
                int temp=frequency[j];
                frequency[j]=frequency[j+1];
                frequency[j+1]=temp;

                temp=primes[j];
                primes[j]=primes[j+1];
                primes[j+1]=temp;
            }
        }
    }
}

void display(int* primes,int* frequency,int primeCount,int mostFrequentPrime){
    cout<<"Prime numbers and their occurrences:"<<endl;
    for(int i=0;i<primeCount;i++){
        cout<<primes[i]<<" -> "<<frequency[i]<<endl;
    }

    cout<<"Most frequently occurring prime: "<<mostFrequentPrime<<endl;

    cout<<"Prime numbers in ascending order of frequency:"<<endl;
    for(int i=0;i<primeCount;i++){
        cout<<primes[i]<<" ";
    }
}

int main(){
    int n;
    cout<<"Enter N: ";
    cin>>n;

    int arr[n];
    cout<<"Enter "<<n<<" integers:"<<endl;
    for(int i=0;i<n;i++){
        cin>>arr[i];
    }

    int primes[n];
    int frequency[n];

    int primeCount=findPrimes(arr,n,primes,frequency);
    int mostFrequentPrime=mostFrequent(primes,frequency,primeCount);

    sortByFrequency(primes,frequency,primeCount);

    display(primes,frequency,primeCount,mostFrequentPrime);

    return 0;
}