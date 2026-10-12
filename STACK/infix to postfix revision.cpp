#include <bits/stdc++.h>
using namespace std;

struct Node
{
    char c;
    Node* next;
};

class Stack
{
    Node* head = nullptr;

public:

    void push(char c)
    {
        Node* temp = new Node;
        temp->c = c;
        temp->next = head;
        head = temp;
    }

    void pop()
    {
        if (head == nullptr)
            return;

        Node* temp = head;
        head = head->next;
        delete temp;
    }

    char top()
    {
        return head->c;
    }

    bool empty()
    {
        return head == nullptr;
    }

    ~Stack()
    {
        while (head != nullptr)
        {
            pop();
        }
    }
};


int precedence(char c)
{
    if (c == '^')
        return 3;

    if (c == '*' || c == '/' || c == '%')
        return 2;

    if (c == '+' || c == '-')
        return 1;

    return 0;
}


bool isOperand(char c)
{
    return (c >= 'A' && c <= 'Z') ||
           (c >= 'a' && c <= 'z') ||
           (c >= '0' && c <= '9');
}


bool isOperator(char c)
{
    return c == '+' ||
           c == '-' ||
           c == '*' ||
           c == '/' ||
           c == '%' ||
           c == '^';
}


int main()
{
    string s;
    cin >> s;

    Stack st;
    string output;

    for (char c : s)
    {
        if (isOperand(c))
        {
            output += c;
        }

        else if (c == '(')
        {
            st.push(c);
        }

        else if (c == ')')
        {
            while (!st.empty() && st.top() != '(')
            {
                output += st.top();
                st.pop();
            }

            if (!st.empty())
                st.pop();
        }

        else if (isOperator(c))
        {
            while (!st.empty() &&
                   st.top() != '(' &&
                   (precedence(st.top()) > precedence(c) ||
                    (precedence(st.top()) == precedence(c) && c != '^')))
            {
                output += st.top();
                st.pop();
            }

            st.push(c);
        }
    }

    while (!st.empty())
    {
        output += st.top();
        st.pop();
    }

    cout << output;

    return 0;
}
