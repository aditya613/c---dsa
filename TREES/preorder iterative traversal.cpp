//using stack LIFO mechanism

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

 //solving using iterative stack approach
class Solution {
public:
    vector<int> preorderTraversal(TreeNode* root) {
        
        vector<int> ans;
        if(root==nullptr) return ans;

        stack<TreeNode*> st;
        st.push(root);

        while(!st.empty()){
            TreeNode* current = st.top();
            ans.push_back(current->val);
            st.pop();

            if(current->right!=nullptr) st.push(current->right);
            if(current->left!=nullptr) st.push(current->left);
        }


        return ans;
    }
};
