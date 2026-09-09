// 2. Add Two Numbers
// Medium
// Topics
// premium lock icon
// Companies
// You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

// You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

// Example 1:


// Input: l1 = [2,4,3], l2 = [5,6,4]
// Output: [7,0,8]
// Explanation: 342 + 465 = 807.
// Example 2:

// Input: l1 = [0], l2 = [0]
// Output: [0]
// Example 3:

// Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
// Output: [8,9,9,9,0,0,0,1]
 

// Constraints:

// The number of nodes in each linked list is in the range [1, 100].
// 0 <= Node.val <= 9
// It is guaranteed that the list represents a number that does not have leading zeros.

#include<bits/stdc++.h>
using namespace std;


//   Definition for singly-linked list.
  struct ListNode {
      int val;
      ListNode *next;
      ListNode() : val(0), next(nullptr) {}
      ListNode(int x) : val(x), next(nullptr) {}
      ListNode(int x, ListNode *next) : val(x), next(next) {}
  };
 

//M-1 storing both the linked list numbers in array lets try
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {

        vector<int> ll1;
        vector<int> ll2;

        // Store first linked list in vector
        while (l1 != nullptr) {
            ll1.push_back(l1->val);
            l1 = l1->next;
        }

        // Store second linked list in vector
        while (l2 != nullptr) {
            ll2.push_back(l2->val);
            l2 = l2->next;
        }

        ListNode* head = nullptr;
        ListNode* current = nullptr;

        int carry = 0;

        for (int i = 0; i < max(ll1.size(), ll2.size()); i++) {

            int temp1 = 0;
            int temp2 = 0;

            if (i < ll1.size()) {
                temp1 = ll1[i];
            }

            if (i < ll2.size()) {
                temp2 = ll2[i];
            }

            int sum = temp1 + temp2 + carry;

            int store = sum % 10;
            carry = sum / 10;

            ListNode* newNode = new ListNode(store);

            // First node
            if (head == nullptr) {
                head = newNode;
                current = newNode;
            }
            // Subsequent nodes
            else {
                current->next = newNode;
                current = newNode;
            }
        }

        // Remaining carry
        if (carry != 0) {
            ListNode* newNode = new ListNode(carry);
            current->next = newNode;
        }

        return head;
    }
};

// Time: O(n + m)
// Extra space: O(n + m) for the vectors


//lets try to solve directly on the linked list
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        
        int carry = 0;
        ListNode* head = nullptr;
        ListNode* current = nullptr;
        while(l1!=nullptr || l2!=nullptr){

            int temp1 = 0, temp2 = 0;
            if(l1!=nullptr){
                temp1 = l1->val;
            }
            if(l2!=nullptr){
                temp2 = l2->val;
            }

            int store = temp1 + temp2 + carry;
            carry = store/10;
            store %= 10;
            
            ListNode* newNode = new ListNode(store);
            if(head==nullptr){
                head = newNode;
            }
            else{
                current->next = newNode;
            }
            current = newNode;


             if(l1!=nullptr){
                l1 = l1->next;
            }
            if(l2!=nullptr){
                l2 = l2->next;
            }

        }
    

      // Remaining carry
        if (carry != 0) {
            ListNode* newNode = new ListNode(carry);
            current->next = newNode;
        }

        return head;
        
    }
};

// Time: O(n+m)
// Auxiliary space: O(1), excluding the output linked list.