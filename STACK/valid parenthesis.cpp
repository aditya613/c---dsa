struct Node{
    char c;
    Node* next;
    Node(char c, Node* next=nullptr): c(c), next(next){}
};

class Stack{
    private:
    Node* head = nullptr;

    public:
        void push(char c){
            Node* temp = new Node(c, head);
            head = temp;
        }

        void pop(){
            Node* temp = head;
            head = head->next;
            delete temp;
        }

        char top(){
            return head->c;
        }

        bool empty(){
            return head==nullptr;
        }

        ~Stack(){
            while(head!=nullptr){
                pop();
            }
        }
};

class Solution {
public:
    bool isValid(string s) {
        Stack stack;
        for(auto c:s){
            if(c=='(' || c=='{' || c=='[')
            stack.push(c);
            else if(c==')' || c=='}' || c==']')
                if(stack.empty())
                return false;
                else{
                if((c==')' && stack.top()=='(') || (c=='}' && stack.top()=='{') || (c==']' && stack.top()=='[')){
                    stack.pop();
                    continue;
                }
                else{
                    return false;
                }
        }
    }

    if(!stack.empty()){
        return false;
    }
    return true;
    }
};