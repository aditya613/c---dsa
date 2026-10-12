#include<bits/stdc++.h>
using namespace std;

class Point; 

class Calculate;

class calculate1;

class Point{
    private:
    int x;
    int y;

    public:
    Point(int x, int y): x(x), y(y){}

    friend float euclideanDistance(const Point& p1, const Point& p2);
    friend Point Calculate::midPoint(const Point& p1, const Point& p2);
};

float euclideanDistance(const Point& p1, const Point& p2){
        return sqrt(pow(p2.x - p1.x, 2) + pow(p2.y - p1.y, 2));
}

class Calculate{
    public:
    Point midPoint(const Point& p1, const Point& p2){
        return Point((p1.x+p2.x)/2, (p1.y+p2.y)/2);
    }
};

class calculate1{
    float DotProduct(const Point& p1, const Point& p2){
        return ((p1.x*p2.x)+(p1.y+p2.y));
    }

    float 2DCrossProduct(const Point& p1, const Point& p2){
        
};