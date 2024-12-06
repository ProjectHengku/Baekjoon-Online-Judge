#include <iostream>

using namespace std;

int main() {
    int A;
    string B;

    cin >> A;
    cin >> B;

    cout << A * stoi(string(1, B[2])) << endl;
    cout << A * stoi(string(1, B[1])) << endl;
    cout << A * stoi(string(1, B[0])) << endl;
    cout << A * stoi(B);

    return 0;
}
