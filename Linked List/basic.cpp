#include <iostream>
using namespace std;

struct Node {
    int data;
    Node* next;
};

void insertAtBeginning(Node*& head, int value) {
    Node* newHead = new Node;

    newHead->data = value;
    newHead->next = head;

    head = newHead;
}

void deleteHeadNode(Node*& head) {
    if (head == nullptr)
        return;

    Node* temp = head;
    head = head->next;

    delete temp;
}

void deleteTailNode(Node*& head){

   if (head == nullptr)
    return;

if (head->next == nullptr) {
    delete head;
    head = nullptr;
    return;
}

    else{
        Node* temp = head;
        while(temp->next->next!=nullptr){
            temp = temp->next;
        }

        Node* toDelete = temp->next;
        temp->next = nullptr;

        delete toDelete;
    }


}


void deleteAtPosition(Node*& head, int position){

    if(head==nullptr){
        return;
    }
    if(position==1){
        deleteHeadNode(head);
    }
    else{
    Node* temp = head;
    for(int i=1;i<position-1;i++){
        temp = temp->next;


    }

    Node* toDelete = temp->next;
   
    if(temp->next->next!=nullptr){
        temp->next = temp->next->next;
    }
    else{
        temp->next = nullptr;
    }
    delete toDelete;

}

}

bool search(Node* head, int value){

    while(head!=nullptr){
        if(head->data == value){
            return true;
        }

        head = head->next;
    }

    return false;

}

int countNodes(Node* head){
    int temp = 0;
    while(head!=nullptr){
        temp++;
        head=head->next;
    }

    return temp;
}

void insertAtPosition(Node*& head, int value, int pos){

    if(pos==1){
        insertAtBeginning(head, value);
        return;
    }
    else if(pos>countNodes(head)){
        return;
    }
    Node* temp = head;

    int i=1;
    while(i<pos-1){
        temp = temp->next;
        i++;
    }

    Node* newNode= new Node;
    newNode->data = value;
    
    newNode->next=temp->next;
    

    temp->next=newNode;


}

void reverseList(Node*& head){
    Node* last;
    while(head!=nullptr){
        last = head;
        head= head->next;
    }


    for(int i=1;i<=countNode)
}
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

    cout << "Original list: ";

    Node* temp = head;

    while (temp != nullptr) {
        cout << temp->data << " ";
        temp = temp->next;
    }

    cout << "\n";

    deleteHeadNode(head);

    cout << "After deleting head: ";

    temp = head;

    while (temp != nullptr) {
        cout << temp->data << " ";
        temp = temp->next;
    }

    cout << "\n";

    // Delete remaining nodes
    while (head != nullptr) {
        Node* temp = head;
        head = head->next;
        delete temp;
    }

    return 0;
}