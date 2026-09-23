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
    ListNode* swapPairs(ListNode* head) {
        
        if(head == nullptr || head->next == nullptr){
            return head;
        }

        ListNode* temp = head;
        ListNode* prev = nullptr;

        head = head->next;
        while(temp != nullptr && temp->next != nullptr){

           
            ListNode* forw = temp->next->next;
            if(prev!=nullptr){
                            prev->next = temp->next; 
                        }
            temp->next->next = temp;
            temp->next = forw;
            prev = temp;

            temp = forw;
        }

        return head;
    }
};