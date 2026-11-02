
#include <iostream>
#include <queue>
#include <algorithm>
using namespace std;

struct Node {
    int key;
    Node* left;
    Node* right;
    int height;

    Node(int val) {
        key = val;
        left = right = nullptr;
        height = 1;
    }
};

// Height of a node
int height(Node* node) {
    if (node == nullptr)
        return 0;

    return node->height;
}

// Balance factor
int getBalance(Node* node) {
    if (node == nullptr)
        return 0;

    return height(node->left) - height(node->right);
}

// Right rotation
Node* rightRotate(Node* y) {
    Node* x = y->left;
    Node* T2 = x->right;

    x->right = y;
    y->left = T2;

    y->height = 1 + max(height(y->left),
                        height(y->right));

    x->height = 1 + max(height(x->left),
                        height(x->right));

    return x;
}

// Left rotation
Node* leftRotate(Node* x) {
    Node* y = x->right;
    Node* T2 = y->left;

    y->left = x;
    x->right = T2;

    x->height = 1 + max(height(x->left),
                        height(x->right));

    y->height = 1 + max(height(y->left),
                        height(y->right));

    return y;
}

// Insertion
Node* insert(Node* root, int key) {
    // 1. Normal BST insertion
    if (root == nullptr)
        return new Node(key);

    if (key < root->key)
        root->left = insert(root->left, key);

    else if (key > root->key)
        root->right = insert(root->right, key);

    else
        return root; // Ignore duplicates

    // 2. Update height
    root->height = 1 + max(height(root->left),
                           height(root->right));

    // 3. Calculate balance factor
    int balance = getBalance(root);

    // LL case
    if (balance > 1 && key < root->left->key)
        return rightRotate(root);

    // RR case
    if (balance < -1 && key > root->right->key)
        return leftRotate(root);

    // LR case
    if (balance > 1 && key > root->left->key) {
        root->left = leftRotate(root->left);
        return rightRotate(root);
    }

    // RL case
    if (balance < -1 && key < root->right->key) {
        root->right = rightRotate(root->right);
        return leftRotate(root);
    }

    return root;
}

// Find minimum-valued node
Node* minValueNode(Node* root) {
    Node* current = root;

    while (current->left != nullptr)
        current = current->left;

    return current;
}

// Deletion
Node* deleteNode(Node* root, int key) {
    // 1. Normal BST deletion
    if (root == nullptr)
        return root;

    if (key < root->key) {
        root->left = deleteNode(root->left, key);
    }
    else if (key > root->key) {
        root->right = deleteNode(root->right, key);
    }
    else {
        // Node has zero or one child
        if (root->left == nullptr || root->right == nullptr) {
    Node* child = root->left
                    ? root->left
                    : root->right;

    delete root;
    return child;
}
        else {
            // Two children: inorder successor
            Node* successor = minValueNode(root->right);

            root->key = successor->key;

            root->right = deleteNode(
                root->right, successor->key
            );
        }
    }

    // If the deleted node was a leaf
    if (root == nullptr)
        return root;

    // 2. Update height
    root->height = 1 + max(height(root->left),
                           height(root->right));

    // 3. Calculate balance factor
    int balance = getBalance(root);

    // LL case
    if (balance > 1 &&
        getBalance(root->left) >= 0)
        return rightRotate(root);

    // LR case
    if (balance > 1 &&
        getBalance(root->left) < 0) {
        root->left = leftRotate(root->left);
        return rightRotate(root);
    }

    // RR case
    if (balance < -1 &&
        getBalance(root->right) <= 0)
        return leftRotate(root);

    // RL case
    if (balance < -1 &&
        getBalance(root->right) > 0) {
        root->right = rightRotate(root->right);
        return leftRotate(root);
    }

    return root;
}

// Search
Node* search(Node* root, int key) {
    if (root == nullptr || root->key == key)
        return root;

    if (key < root->key)
        return search(root->left, key);

    return search(root->right, key);
}

// Inorder: Left, Root, Right
void inorder(Node* root) {
    if (root == nullptr)
        return;

    inorder(root->left);
    cout << root->key << " ";
    inorder(root->right);
}

// Preorder: Root, Left, Right
void preorder(Node* root) {
    if (root == nullptr)
        return;

    cout << root->key << " ";
    preorder(root->left);
    preorder(root->right);
}

// Postorder: Left, Right, Root
void postorder(Node* root) {
    if (root == nullptr)
        return;

    postorder(root->left);
    postorder(root->right);
    cout << root->key << " ";
}

// Level-order traversal (BFS)
void levelOrder(Node* root) {
    if (root == nullptr)
        return;

    queue<Node*> q;
    q.push(root);

    while (!q.empty()) {
        Node* current = q.front();
        q.pop();

        cout << current->key << " ";

        if (current->left != nullptr)
            q.push(current->left);

        if (current->right != nullptr)
            q.push(current->right);
    }
}

// Display tree sideways
void display(Node* root, int space = 0) {
    if (root == nullptr)
        return;

    space += 5;

    display(root->right, space);

    cout << "\n";
    for (int i = 5; i < space; i++)
        cout << " ";

    cout << root->key
         << "(h=" << root->height << ")";

    display(root->left, space);
}

// Free all allocated memory
void destroyTree(Node* root) {
    if (root == nullptr)
        return;

    destroyTree(root->left);
    destroyTree(root->right);
    delete root;
}

int main() {
    Node* root = nullptr;
    int choice, key;

    do {
        cout << "\n\n--- AVL TREE MENU ---\n";
        cout << "1. Insert\n";
        cout << "2. Delete\n";
        cout << "3. Inorder\n";
        cout << "4. Preorder\n";
        cout << "5. Postorder\n";
        cout << "6. Level-order\n";
        cout << "7. Search\n";
        cout << "8. Display tree\n";
        cout << "0. Exit\n";
        cout << "Enter choice: ";
        cin >> choice;

        switch (choice) {
            case 1:
                cout << "Enter key: ";
                cin >> key;
                root = insert(root, key);
                break;

            case 2:
                cout << "Enter key to delete: ";
                cin >> key;
                root = deleteNode(root, key);
                break;

            case 3:
                inorder(root);
                cout << "\n";
                break;

            case 4:
                preorder(root);
                cout << "\n";
                break;

            case 5:
                postorder(root);
                cout << "\n";
                break;

            case 6:
                levelOrder(root);
                cout << "\n";
                break;

            case 7:
                cout << "Enter key to search: ";
                cin >> key;

                if (search(root, key))
                    cout << "Found\n";
                else
                    cout << "Not found\n";
                break;

            case 8:
                display(root);
                cout << "\n";
                break;

            case 0:
                destroyTree(root);
                cout << "Exiting...\n";
                break;

            default:
                cout << "Invalid choice\n";
        }

    } while (choice != 0);

    return 0;
}
