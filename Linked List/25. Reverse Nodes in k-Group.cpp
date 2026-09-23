#include<bits/stdc++.h>
using namespace std;

struct Node{
    int data;
    Node* next;
};

Node* reverseBetween(ListNode* head, int left, int right) {

        if(head==nullptr || head->next==nullptr){
            return head;
        }
        Node* prev = nullptr;
        Node* curr = head;

        for(int i=1;i<left;i++){
            curr = curr->next;
        }
        Node* start = curr;
        Node* next = new Node;
        while(left<=right){
            next = curr->next;
            curr->next = prev;
            curr = next;
        }

        start->next = next;


        return head;

    }
int main(){

    int n = k;

    
}