#include <iostream>

using namespace std;

int main() {
    int A, B;
    int C;

    cin >> A >> B;
    cin >> C;

    B += C;
    A += B / 60;
    B %= 60;

    cout << A % 24 << " " << B << endl;

    return 0;
}
