#include <iostream>
using namespace std;


void insertAtBeginning(Node*& head, int value){

    Node* newHead = new Node;
    newHead->data = value;
    newHead->next = &head;

    head = newHead;
}
struct Node {
    int data;
    Node* next;
};

int main() {
    Node* head = new Node;
    Node* second = new Node;
    Node* third = new Node;

    head->data = 10;
    head->next = second;

    second->data = 20;
    second->next = third;

    third->data = 30;
    third->next = nullptr;

    Node* temp = head;

    while (temp != nullptr) {
        cout << temp->data << " ";
        temp = temp->next;
    }

    delete third;
    delete second;
    delete head;

    return 0;
}