#include <bits/stdc++.h>
using namespace std;

bool checkDuplicate(const vector<int>& arr, int size, int value)
{
    for (int i = 0; i < size; i++)
    {        if (arr[i] == value)       return true;
    }
    return false;
}

int removeDuplicates(vector<int>& arr, int n)
{
    int newSize = 0;
    for (int i = 0; i < n; i++)
    {
        if (!checkDuplicate(arr, newSize, arr[i]))
        {
            
        arr[newSize] = arr[i];
            newSize++; }
    }
    return newSize;
}

void display(const vector<int>& arr, int n)
{
    cout << "Array after removing duplicates: ";
    for (int i = 0; i < n; i++)
        cout << arr[i] << " ";
}

int main()
{
    int n;
    cout << "Enter number of elements: ";
    cin >> n;


    vector<int> arr(n);

    for (int i = 0; i < n; i++)
        cin >> arr[i];
    n = removeDuplicates(arr, n);
    display(arr, n);

    return 0;
}