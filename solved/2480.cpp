#include <iostream>

using namespace std;

int main() {
    short a, b, c;

    cin >> a >> b >> c;

    if (a == b && b == c) {
        cout << 10000 + a * 1000 << endl;
    } else if (a == b || a == c) {
        cout << 1000 + a * 100 << endl;
    } else if (b == c) {
        cout << 1000 + b * 100 << endl;
    } else {
        cout << max(a, max(b, c)) * 100 << endl;
    }

    return 0;
}