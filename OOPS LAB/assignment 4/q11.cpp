#include <bits/stdc++.h>
using namespace std;

class Candidate {
    int candidateID;
    int writtenTestMarks;
    int interviewMarks;

public:

    Candidate(int id, int marks1, int marks2) {
        candidateID = id;
        writtenTestMarks = marks1;
        interviewMarks = marks2;
    }

    void comparison(const Candidate &c1, const Candidate &c2) {
        int total1 = c1.writtenTestMarks + c1.interviewMarks;
        int total2 = c2.writtenTestMarks + c2.interviewMarks;

        if (total1 > total2) {
            cout << "Candidate " << c1.candidateID << " has higher total score." << endl;
        }
        else if (total2 > total1) {
            cout << "Candidate " << c2.candidateID << " has higher total score." << endl;
        }
        else {
            if (c1.writtenTestMarks > c2.writtenTestMarks) {
                cout << "Candidate " << c1.candidateID << " wins by written-test marks." << endl;
            }
            else if (c2.writtenTestMarks > c1.writtenTestMarks) {
                cout << "Candidate " << c2.candidateID << " wins by written-test marks." << endl;
            }
            else {
                cout << "Both candidates have the same score." << endl;
            }
        }
        cout << "----------------------------------------------" << endl;
    }
};

int main() {

    Candidate c1(124, 80, 75);
    Candidate c2(125, 90, 80);

    c1.comparison(c1, c2);

    Candidate c3(126, 80, 80);
    Candidate c4(127, 90, 75);

    c3.comparison(c3, c4);

    Candidate c5(128, 80, 75);
    Candidate c6(129, 90, 65);

    c5.comparison(c5, c6);

    return 0;
}