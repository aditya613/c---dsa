#include<bits/stdc++.h>
using namespace std;

void palidrome_number_pyramid(int n){

    for(int i=1;i<=n;i++){

        for (int j = 1; j <= n - i; j++) {
                cout << " ";
            }

        for(int k=i;k>=1;k--){
            cout<<k<<" ";
        }
        for(int z=2;z<=i;z++){
            cout<<z<<" ";
        }

        cout<<endl;
    }

}


void alpha_palindromic_pyramid(int n){

    char arr[] = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'};
    for(int i=1;i<=n;i++){

        for (int j = 1; j <= n - i; j++) {
                cout << " ";
            }

        for(int k=i;k>=1;k--){
            cout<<arr[k-1]<<" ";
        }
        for(int z=2;z<=i;z++){
            cout<<arr[z-1]<<" ";
        }

        cout<<endl;
    }


}
void hollow_number_pyramid(int n){
    for(int i = 1; i <= n; i++){
        for(int j = 1; j <= n - i; j++){
            cout << " ";
        }
        if(i == 1){
            cout << "1";
        }
        else if(i == n){
            for(int j = 1; j <= 2 * n - 1; j++){
                cout << "1";
            }
        }
        else{
            cout << "1";
            for(int j = 1; j <= 2 * (i - 1) - 1; j++){
                cout << " ";
            }
            cout << "1";
        }
        cout << endl;
    }
}

void inverted_number_pyramid(int n){
    for(int i = 1; i <= n; i++){
        for(int j = 1; j <= 2 * (i - 1); j++){
            cout << " ";
        }
        for(int j = i; j <= n; j++){
            cout << j << " ";
        }
        cout << endl;
    }
}

void diamond_number_pattern(int n){
    for(int i = 1; i <= n; i++){
        for(int j = 1; j <= n - i; j++){
            cout << " ";
        }
        for(int j = 1; j <= i; j++){
            cout << j << " ";
        }
        cout << endl;
    }
    for(int i = n - 1; i >= 1; i--){
        for(int j = 1; j <= n - i; j++){
            cout << " ";
        }
        for(int j = 1; j <= i; j++){
            cout << j << " ";
        }
        cout << endl;
    }
}

void hollow_diamond_pattern(int n){
    for(int i = 1; i <= n; i++){
        for(int j = 1; j <= n - i; j++){
            cout << " ";
        }
        for(int j = 1; j <= 2 * i - 1; j++){
            if(j == 1 || j == 2 * i - 1){
                cout << "*";
            } else {
                cout << " ";
            }
        }
        cout << endl;
    }
    for(int i = n - 1; i >= 1; i--){
        for(int j = 1; j <= n - i; j++){
            cout << " ";
        }
        for(int j = 1; j <= 2 * i - 1; j++){
            if(j == 1 || j == 2 * i - 1){
                cout << "*";
            } else {
                cout << " ";
            }
        }
        cout << endl;
    }
}
int main(){


    cout<<"Pyramid Patterns code menu "<<endl;
    cout<<"1. Palindromic Number Pyramid"<<endl;
    cout<<"2. Alphabetic Palindromic Pyramid"<<endl;
    cout<<"3. Hollow Number Pyramid"<<endl;
    cout<<"4. Inverted Number Pyramid"<<endl;
    cout<<"5. Diamond Number Pattern"<<endl;
    cout<<"6. Hollow Diamond Pattern"<<endl;
    cout<<"7. EXIT"<<endl<<endl;
    while(true){
        cout<<"Enter Number to see output: ";
        int temp;
        cin>>temp;
        cout<<endl;

        cout<<"Enter N: ";
        int n;
        cin>>n;
        switch(temp){
            case 1:{
                palidrome_number_pyramid(n);
                break;
               }
            case 2:{
                alpha_palindromic_pyramid(n);
                break;
            }
            case 3:{
                hollow_number_pyramid(n);
                break;
            }
            case 4: {
                inverted_number_pyramid(n);
                break;
            }
            case 5: {

                diamond_number_pattern(n);
                break;

            }
            case 6: {
                hollow_diamond_pattern(n);
                break;    
                }
             case 7: {
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