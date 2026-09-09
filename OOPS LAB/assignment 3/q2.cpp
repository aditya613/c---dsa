#include<bits/stdc++.h>
using namespace std;

int findSecondLargest(int arr[], int n) {

    int largest = arr[0];
    int secondLargest = 0;
    bool foundSecond = false;

    for(int i = 1; i < n; i++) {

        if(arr[i] > largest) {

            secondLargest = largest;
            largest = arr[i];
            foundSecond = true;
        }
        else if(arr[i] < largest) {

            if(!foundSecond || arr[i] > secondLargest) {
                secondLargest = arr[i];
                foundSecond = true;
            }
        }
    }

    if(!foundSecond) {
        return -1;
    }

    return secondLargest;
}
int main() {

    int arr[] = {1,4,0,8,7,5,6,6,9,8,11,12};



    int n = sizeof(arr) / sizeof(arr[0]);
    cout << findSecondLargest(arr, n);
    return 0;
}