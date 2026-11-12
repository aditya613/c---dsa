#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;

    cout << "Enter number of elements: ";
    cin >> n;

    int *arr = new int[n];

    cout << "Enter array elements: ";
    for (int i = 0; i < n; i++) {
        cin >> *(arr + i);
    }

    int largest = *arr;
    int smallest = *arr;
    int sum = 0;

    for (int i = 0; i < n; i++) {
        if (*(arr + i) > largest)
            largest = *(arr + i);

        if (*(arr + i) < smallest)
            smallest = *(arr + i);

        sum += *(arr + i);
    }

    float average = (float)sum / n;

    cout << "Largest element: " << largest << endl;
    cout << "Smallest element: " << smallest << endl;
    cout << "Average: " << average << endl;

    delete[] arr;

    return 0;
}