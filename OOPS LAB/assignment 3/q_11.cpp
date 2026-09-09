#include<iostream>
using namespace std;


void moveZeros(int* arr, int n) {
    int index = 0;
    for(int i = 0; i < n; i++) {
        if(arr[i] != 0) {
    swap(arr[index], arr[i]);
          index++;
        }}
}


void display(int* arr, int n) {
    for(int i = 0; i < n; i++) {
       
        cout << arr[i] << " ";
    }
}



int main() {
    int arr[8] = {0, 5, 0, 2, 8, 0, 3, 0};
    int n = 8;

    cout << "Before: ";
    display(arr, n);

    moveZeros(arr, n);

    cout << "\nAfter: ";
    display(arr, n);

    return 0;
}