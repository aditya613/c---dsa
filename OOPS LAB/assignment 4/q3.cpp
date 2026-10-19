#include <bits/stdc++.h>
using namespace std;

class circle;
class point{
private:
    int Xcord;
    int Ycord;

public:
    point(int x, int y){
        Xcord = x;
        Ycord = y;
    }

    friend class circle;
    friend bool pointInsideCircle(point p, circle c);
};
class circle{
private:
    int Xcord;
    int Ycord;
    int radius;

public:
    circle(point &pnt, int r){
        Xcord = pnt.Xcord;
        Ycord = pnt.Ycord;

        if(r > 0){
            radius = r;
        }
        else{
            cout << "INVALID RADIUS" << endl;
            radius = 0;
        }
    }

    friend bool pointInsideCircle(point p, circle c);
    friend bool twoIntersectionCircle(circle c1, circle c2);
};
bool pointInsideCircle(point p, circle c){
    int dx = p.Xcord - c.Xcord;
    int dy = p.Ycord - c.Ycord;

    int dst = dx * dx + dy * dy;
    int range = c.radius * c.radius;

    return dst <= range;
}
bool twoIntersectionCircle(circle c1, circle c2){
    int dx = c1.Xcord - c2.Xcord;
    int dy = c1.Ycord - c2.Ycord;

    int dst = dx * dx + dy * dy;

    int sum = c1.radius + c2.radius;
    int diff = abs(c1.radius - c2.radius);

    return dst <= sum * sum && dst >= diff * diff;
}
int main(){
    point p1(0, 0);
    point p2(5, 0);

    circle c1(p1, 4);
    circle c2(p2, 3);

    point p3(2, 2);

    if(pointInsideCircle(p3, c1))
        cout << "Point is inside circle" << endl;
    else
        cout << "Point is outside circle" << endl;
    if(twoIntersectionCircle(c1, c2))
        cout << "Circles intersect" << endl; 
    else
        cout << "Circles do not intersect" << endl;
    return 0;
}