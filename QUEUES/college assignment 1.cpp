#include <iostream>
using namespace std;

class Queue {
private:
    struct Node {
        int data;
        Node* next;

        Node(int value) {
            data = value;
            next = nullptr;
        }
    };

    Node* front;
    Node* rear;

public:
    Queue() {
        front = nullptr;
        rear = nullptr;
    }

    // Insert element at rear
    void enqueue(int value) {
        Node* newNode = new Node(value);

        if (rear == nullptr) {
            front = rear = newNode;
            return;
        }

        rear->next = newNode;
        rear = newNode;
    }

    // Remove element from front
    void dequeue() {
        if (front == nullptr) {
            cout << "Queue is empty\n";
            return;
        }

        Node* temp = front;
        cout << "Removed: " << temp->data << endl;

        front = front->next;

        // If queue becomes empty
        if (front == nullptr) {
            rear = nullptr;
        }

        delete temp;
    }

    // Get front element
    int getFront() {
        if (front == nullptr) {
            cout << "Queue is empty\n";
            return -1;
        }

        return front->data;
    }

    // Check if empty
    bool isEmpty() {
        return front == nullptr;
    }

    // Display queue
    void display() {
        Node* temp = front;

        while (temp != nullptr) {
            cout << temp->data << " ";
            temp = temp->next;
        }

        cout << endl;
    }
};

int main() {
    Queue q;

    q.enqueue(10);
    q.enqueue(20);
    q.enqueue(30);
    q.enqueue(40);
    q.enqueue(50);

    cout << "Queue: ";
    q.display();

    cout << "Front: " << q.getFront() << endl;

    q.dequeue();
    q.dequeue();

    cout << "Queue after dequeue: ";
    q.display();

    q.enqueue(60);
    q.enqueue(70);

    cout << "Queue after enqueue: ";
    q.display();

    return 0;
}