#include<bits/stdc++.h>
using namespace std;

struct Node{
    int data;
    Node* next;
};

class Stack{
    Node* head = nullptr;

    public:
    void enqueue(int val){
        Node* temp = new Node;
        temp->data = val;
        temp->next = head;
        head= temp;
    }

    int dequeue(){
        Node* temp = head;
        head = head->next;
        int val = temp->data;
        delete temp;
        return val;
    }

    bool isEmpty(){
        return head==nullptr;
    }

    int top(){
        if(!isEmpty()){
            return head->data;
        }
        return -1;
    }
};



//try normal array O(n*n) solution
//brute force solution

class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& nums1,
                                   vector<int>& nums2) {
        unordered_map<int, int> mpp;

        for (int i = 0; i < nums2.size(); i++) {
            mpp[nums2[i]] = -1;

            for (int j = i + 1; j < nums2.size(); j++) {
                if (nums2[j] > nums2[i]) {
                    mpp[nums2[i]] = nums2[j];
                    break;
                }
            }
        }

        vector<int> ans(nums1.size());

        for (int i = 0; i < nums1.size(); i++) {
            ans[i] = mpp[nums1[i]];
        }

        return ans;
    }
};

//above approach 
// Let \(n = |\text{nums2}|\) and \(m = |\text{nums1}|\).
// - Time: \(O(n^2+m)\) expected, including map operations.
// - Space: \(O(n)\) for the map and \(O(m)\) for the output.

//approach 2 brute force still but lets try better

class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
        
        vector<int> ans(nums1.size(), -1);
        for(int i=0;i<nums1.size();i++){

            bool start = false;
            for(int j=0;j<nums2.size();j++){
                if(nums1[i] == nums2[j]){
                    start = true;
                }

                if(start){
                    if(nums2[j]>nums1[i]){ ans[i] = nums1[j];
                    break;
                    }
                }
            }
        }

        return ans;
    }
};

//for above approach
// Let \(m = |\text{nums1}|\) and \(n = |\text{nums2}|\).
// - Time: \(O(mn)\) worst case.
// - Auxiliary space: \(O(1)\), excluding the output array.


//for LC496
class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
        
        stack<int> st;

        vector<int> ans(nums1.size(), -1);
        unordered_map<int,int> fullAns;

        for(int i=nums2.size()-1; i>=0;i--){

            while(!st.empty() && st.top()<=nums2[i]){
                st.pop();
            }

            if(!st.empty()) fullAns[nums2[i]] = st.top();
            else fullAns[nums2[i]] = -1;
            st.push(nums2[i]);
        }

        for(int i=0;i<nums1.size();i++){
            ans[i] = fullAns[nums1[i]];
        }

        return ans;
    }
};