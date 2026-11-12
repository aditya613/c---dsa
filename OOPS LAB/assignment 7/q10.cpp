#include <bits/stdc++.h>
using namespace std;

class Shape {
public:
    virtual void calculateArea() {
        cout << "Calculating area" << endl;
    }
};

class Rectangle : public Shape {
public:
    float length, breadth;

    void calculateArea() override {
        cout << "Enter length and breadth: ";
        cin >> length >> breadth;

        cout << "Area of Rectangle: " << length * breadth << endl;
    }
};

class Circle : public Shape {
public:
    float radius;

    void calculateArea() override {
        cout << "Enter radius: ";
        cin >> radius;

        cout << "Area of Circle: " << 3.14 * radius * radius << endl;
    }
};

class Triangle : public Shape {
public:
    float base, height;

    void calculateArea() override {
        cout << "Enter base and height: ";
        cin >> base >> height;

        cout << "Area of Triangle: " << 0.5 * base * height << endl;
    }
};

int main() {
    Rectangle r;
    Circle c;
    Triangle t;

    Shape *ptr;

    ptr = &r;
    ptr->calculateArea();

    ptr = &c;
    ptr->calculateArea();

    ptr = &t;
    ptr->calculateArea();

    return 0;
}