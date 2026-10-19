#include <bits/stdc++.h>
using namespace std ; 

const double PI = 3.14 ;

double rectArea(double length , double breadth){
    return length * breadth ;
}

double rectPerimeter(double length , double breadth){
    return 2*(length + breadth);
}

double squareArea(int side){
    return side * side ;
}

double squarePerimeter(int side){
    return 4 * side ;
}

double circleArea(int radius){
    return PI * radius * radius ;
}

double circlePerimeter(int radius){
    return 2 * PI * radius ;
}