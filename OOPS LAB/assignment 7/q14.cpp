#include <bits/stdc++.h>
using namespace std;

class Product {
public:
    int productID;
    string name;
    float price;

    Product(int id, string n, float p) {
        productID = id;
        name = n;
        price = p;
    }

    virtual void calculateFinalPrice() = 0;
};

class Electronics : public Product {
public:
    int warranty;

    Electronics(int id, string n, float p, int w)
        : Product(id, n, p) {
        warranty = w;
    }

    void calculateFinalPrice() override {
        float discount = price * 0.10;
        float finalPrice = price - discount;

        cout << "\nElectronics Details" << endl;
        cout << "Product ID: " << productID << endl;
        cout << "Name: " << name << endl;
        cout << "Price: " << price << endl;
        cout << "Warranty: " << warranty << " years" << endl;
        cout << "Discount: " << discount << endl;
        cout << "Final Price: " << finalPrice << endl;
    }
};

class Clothing : public Product {
public:
    string size;

    Clothing(int id, string n, float p, string s)
        : Product(id, n, p) {
        size = s;
    }

    void calculateFinalPrice() override {
        float discount = price * 0.20;
        float finalPrice = price - discount;

        cout << "\nClothing Details" << endl;
        cout << "Product ID: " << productID << endl;
        cout << "Name: " << name << endl;
        cout << "Price: " << price << endl;
        cout << "Size: " << size << endl;
        cout << "Discount: " << discount << endl;
        cout << "Final Price: " << finalPrice << endl;
    }
};

int main() {
    Product *ptr[2];

    ptr[0] = new Electronics(101, "Laptop", 60000, 2);
    ptr[1] = new Clothing(102, "Shirt", 2000, "M");

    for (int i = 0; i < 2; i++) {
        ptr[i]->calculateFinalPrice();
    }

    for (int i = 0; i < 2; i++) {
        delete ptr[i];
    }

    return 0;
}