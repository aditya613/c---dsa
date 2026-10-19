#include <bits/stdc++.h> 
using namespace std ; 

class ShoppingCart{
private:
    int customerID;
    double purchaseAmount ; 
    string itemInfo ; 
    string customerCategory ; 
public:

    ShoppingCart(int a , double b , string s1 , string s2){
        customerID = a ; 
        purchaseAmount = b ; 
        itemInfo = s1 ; 
        customerCategory = s2 ;
    }

    void display(){
        cout << "Customer ID : " << customerID << endl;
        cout << "purchase Amount : " << purchaseAmount << endl;
        cout << "Item Info : " << itemInfo << endl;
        cout << "customer category : " << customerCategory << endl;
    }
    friend class DiscountManager ; 

}; 
class DiscountManager{
public:
    void applyDiscount(ShoppingCart &cart){
        int discount = 0 ;

        if(cart.purchaseAmount >= 7500){
            discount += 20 ;
        }else if(cart.purchaseAmount >= 5000){
            discount += 15 ;
        }else if(cart.purchaseAmount >= 2500){
            discount += 10;
        }

        if(cart.customerCategory == "Premium"){
            discount += 5 ; 
        }else if(cart.customerCategory == "VIP"){
            discount += 10 ; 
        }

        int discountamount = cart.purchaseAmount * (discount) / 100 ;
        int minAmount = 500 ;

        int totalAmount = cart.purchaseAmount - discountamount ;
        if(totalAmount >= minAmount){
            cout << "Discount is " << discount << "%" << endl;
            cout << "Amount to be paid now is " << totalAmount << endl; 
        }else{
            cout << "Discount not applicable" << endl;
        }
    }
};

int main(){
    ShoppingCart cart1(12 , 4000 , "Laptop" , "VIP");
    DiscountManager manager ; 
    cart1.display();
    manager.applyDiscount(cart1);
    return 0 ;

}