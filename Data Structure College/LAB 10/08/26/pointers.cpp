#include<bits/stdc++.h>
using namespace std;


void swapNumbers(int* a, int* b)
{
    int temp = *a;

    *a = *b;

    *b = temp;
}


int main(){

    int x=10;

    //declaring an integer pointer
    int* pointer = &x;

    cout<<pointer;

        cout << "Value stored in pointer: " << pointer << endl;
    cout << "Value pointed to by pointer: " << *pointer << endl;


    //changing value through pointer

    *pointer = 50;


    cout<<x;



    //swaping using pointers and address

    int x = 10;
    int y = 20;

    cout << x << endl;
    cout << y << endl;

    swapNumbers(&x, &y);

    cout << endl;

    cout << "After swapping:" << endl;
    cout << "x = " << x << endl;
    cout << "y = " << y << endl;

    

    //arrays using pointers
     int arr[5] = {10, 20, 30, 40, 50};

    int* p = arr;

    for (int i = 0; i < 5; i++)
    {
        cout << *(p + i) << endl;
    }


    

}