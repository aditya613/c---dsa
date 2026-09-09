#include <iostream>
#include <stack>
#include <string>
using namespace std;

class Stack
{
    int arr[100];
    int top;

public:

    Stack()
    {
        top = -1;
    }

    void push(int x)
    {
        if (top == 99)
        {
            cout << "Stack is full\n";
            return;
        }

        arr[++top] = x;
    }

    void pop()
    {
        if (top == -1)
        {
            cout << "Stack is empty\n";
            return;
        }

        cout << "Deleted: " << arr[top] << endl;
        top--;
    }

    void peek()
    {
        if (top == -1)
        {
            cout << "Stack is empty\n";
            return;
        }

        cout << "Top: " << arr[top] << endl;
    }

    void display()
    {
        if (top == -1)
        {
            cout << "Stack is empty\n";
            return;
        }

        cout << "Stack: ";

        for (int i = top; i >= 0; i--)
            cout << arr[i] << " ";

        cout << endl;
    }
};


// Check valid parentheses
bool validParentheses(string s)
{
    stack<char> st;

    for (char c : s)
    {
        if (c == '(' || c == '[' || c == '{')
        {
            st.push(c);
        }
        else if (c == ')' || c == ']' || c == '}')
        {
            if (st.empty())
                return false;

            char x = st.top();
            st.pop();

            if (c == ')' && x != '(')
                return false;

            if (c == ']' && x != '[')
                return false;

            if (c == '}' && x != '{')
                return false;
        }
    }

    return st.empty();
}


// Postfix evaluation
int postfix(string exp)
{
    stack<int> st;

    for (char c : exp)
    {
        if (c >= '0' && c <= '9')
        {
            st.push(c - '0');
        }
        else
        {
            int b = st.top();
            st.pop();

            int a = st.top();
            st.pop();

            if (c == '+')
                st.push(a + b);

            else if (c == '-')
                st.push(a - b);

            else if (c == '*')
                st.push(a * b);

            else if (c == '/')
                st.push(a / b);
        }
    }

    return st.top();
}


int main()
{
    Stack s;

    s.push(10);
    s.push(20);
    s.push(30);

    s.display();

    s.peek();

    s.pop();

    s.display();


    string brackets;

    cout << "\nEnter brackets: ";
    cin >> brackets;

    if (validParentheses(brackets))
        cout << "Valid Parentheses\n";
    else
        cout << "Invalid Parentheses\n";


    string exp;

    cout << "\nEnter postfix expression: ";
    cin >> exp;

    cout << "Answer: " << postfix(exp) << endl;

    return 0;
}
