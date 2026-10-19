#include <iostream>
#include <string>
using namespace std;

class SmartDevice {
private:
    int deviceID;

protected:
    float powerConsumption;
    bool status;

public:
    SmartDevice(int id, float power) {
        deviceID = id;
        powerConsumption = power;
        status = false;
    }

    void turnOn() {
        status = true;
    }

    void turnOff() {
        status = false;
    }

    void displayStatus() {
        cout << "Device ID: " << deviceID << endl;
        cout << "Power Consumption: " << powerConsumption << " W" << endl;
        cout << "Status: " << (status ? "ON" : "OFF") << endl;
    }
};

class SmartAC : protected SmartDevice {
protected:
    float temperature;
    string operatingMode;

public:
    SmartAC(int id, float power, float temp, string mode)
        : SmartDevice(id, power) {
        temperature = temp;
        operatingMode = mode;
    }

    void setTemperature(float temp) {
        temperature = temp;
    }

    void setMode(string mode) {
        operatingMode = mode;
    }
};

class AIEnabledAC : public SmartAC {
private:
    bool energyOptimization;

public:
    AIEnabledAC(int id, float power, float temp, string mode)
        : SmartAC(id, power, temp, mode) {
        energyOptimization = false;
    }

    void enableOptimization() {
        energyOptimization = true;
        powerConsumption *= 0.9;
    }

    void switchOn() {
        turnOn();
    }

    void switchOff() {
        turnOff();
    }

    void display() {
        displayStatus();
        cout << "Temperature: " << temperature << " C" << endl;
        cout << "Operating Mode: " << operatingMode << endl;
        cout << "Energy Optimization: "
             << (energyOptimization ? "Enabled" : "Disabled") << endl;
    }
};

int main() {
    AIEnabledAC ac(101, 1500, 24, "Cool");

    AIEnabledAC* p1 = &ac;
    SmartAC* p2 = &ac;

    p1->switchOn();
    p1->display();

    p1->enableOptimization();

    cout << "\nAfter Optimization" << endl;
    p1->display();

    p2->setTemperature(22);
    p1->display();

    return 0;
}
