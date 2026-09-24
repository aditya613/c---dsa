#include <bits/stdc++.h>
using namespace std;

struct Node {
    char val;
    Node* next;
};

class Self_Stack {

private:
    Node* topNode = nullptr;

public:

    char top() {
        return (topNode == nullptr) ? '\0' : topNode->val;
    }

    void push(char element) {
        Node* temp = new Node;
        temp->val = element;
        temp->next = topNode;
        topNode = temp;
    }

    void pop() {
        if (topNode == nullptr) {
            return;
        }

        Node* temp = topNode;
        topNode = topNode->next;
        delete temp;
    }

    bool empty() {
        return topNode == nullptr;
    }

    // Destructor to free all nodes
    ~Self_Stack() {
        while (topNode != nullptr) {
            Node* temp = topNode;
            topNode = topNode->next;
            delete temp;
        }
    }
};


class InfixToPostfix {

private:
    Self_Stack st;
    string s;

    int precedence(char c) {
        if (c == '^')
            return 3;
        if (c == '*' || c == '/' || c == '%')
            return 2;
        if (c == '+' || c == '-')
            return 1;
        return -1;
    }

    bool isOperator(char c) {

        return c == '+' ||
               c == '-' ||
               c == '*' ||
               c == '/' ||
               c == '%' ||
               c == '^';
    }

public:
    InfixToPostfix(string s) {
        this->s = s;
    }
    string convert() {
        string output = "";
        for (char c : s) {

            if ((c >= 'A' && c <= 'Z') ||
                (c >= 'a' && c <= 'z') ||
                (c >= '0' && c <= '9')) {

                output += c;
            }
            else if (c == '(') {
                st.push(c);}
            else if (c == ')') {
                while (!st.empty() && st.top() != '(') {
                    output += st.top();
                    st.pop();
                }

                if (!st.empty()) {
                    st.pop();
                }
            }

            else if (isOperator(c)) {

                while (!st.empty() &&
                       st.top() != '(' &&
                       precedence(st.top()) >= precedence(c)) {

                    output += st.top();
                    st.pop();
                }

                st.push(c);
            }
        }

        // 5. Empty remaining operators
        while (!st.empty()) {

            output += st.top();
            st.pop();
        }

        return output;
    }
};


int main() {

    string expression;

    cout << "Enter infix expression: ";
    cin >> expression;

    InfixToPostfix converter(expression);

    cout << "Postfix expression: "
         << converter.convert()
         << endl;

    return 0;
}
