
#include <iostream>
using namespace std;

class Device {
public:
    void show() {
        cout << "Device class" << endl;
    }
};

class Laptop : public Device {
};

class Server : protected Device {
public:
    Device* convert() {
        return this;
    }
};

class EmbeddedSystem : private Device {
public:
    Device* convert() {
        return this;
    }
};

int main() {
    Laptop laptop;
    Server server;
    EmbeddedSystem embedded;

    Device* p1 = &laptop;
    p1->show();

    Device* p2 = server.convert();
    p2->show();

    Device* p3 = embedded.convert();
    p3->show();

    return 0;
}
