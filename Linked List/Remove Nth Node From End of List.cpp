//two traversal approach
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    int countNodes(ListNode* node){
        int cnt = 0;
        while(node!=nullptr){
            cnt++;
            node=node->next;
        }
        return cnt;
    }


    ListNode* removeNthFromEnd(ListNode* head, int n) {
        
        if(n==1 && head->next==nullptr){
            head = nullptr;
            return head;
        }
        int cnt = countNodes(head);
        
        if(n==cnt){
            return head->next;
        }
        ListNode* temp = head;
        while((cnt-n)>1){
            temp = temp->next;
            cnt--;
        }
        temp->next = temp->next->next; 

        return head;
    }
};




//single traversal tortoise approacch
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode dummy(0, head);
        ListNode* fast = &dummy;
        ListNode* slow = &dummy;

        for(int i = 0; i < n; i++) {
            fast = fast->next;
        }

        while(fast->next != nullptr) {
            fast = fast->next;
            slow = slow->next;
        }

        slow->next = slow->next->next;

        return dummy.next;
    }
};
// Why this is better
// Your approach:

// Traverse list to count → O(L)
// Traverse again to find node → O(L)
// Total → O(2L)
// Two-pointer approach:

// Move fast n nodes ahead.
// Move fast and slow together.
// When fast reaches the end, slow is exactly before the node to remove.
// So:

// Time: O(L)
// Space: O(1)