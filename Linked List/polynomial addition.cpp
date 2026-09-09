#include<bits/stdc++.h>
using namespace std;


class Node{
    public:
    int pow;
    int coeff;
    Node* next;

    Node(int pow, int coeff){
        this->pow = pow;
        this->coeff = coeff;
        this->next = nullptr;
    }

    Node(int pow, int coeff, Node* next){
        this->pow = pow;
        this->coeff = coeff;
        this->next = next;
    }
};
int main(){

//first polynomial 5X^12 + 2X^9 - X^3
//second polynomial 5X^11 - 4X^9 + 2X^3 - X

//lets make first polynomial node
Node* head1 = new Node(12, 5);

Node* newNode = new Node(9,2);
head1->next = newNode;
Node* newnewNode = new Node(3,-1);
newNode->next = newnewNode;


//lets make second polynomial

Node* head2 = new Node(11, 5);

Node* newNode = new Node(9,-4);
head2->next = newNode;
Node* newnewNode = new Node(3,2);
newNode->next = newnewNode;

Node* newnewnewNode = new Node(1,-1);
newnewNode->next = newnewnewNode;


//lets make third node of adding poly1+poly2
Node* head3 = new Node;
while(head1!=nullptr && head2!=nullptr){
    if(head1->pow>head2->pow){

    }
}


}