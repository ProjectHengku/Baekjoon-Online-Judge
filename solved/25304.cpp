#include <iostream>

using namespace std;

int main() {
    int X;
    short N;

    cin >> X;
    cin >> N;

    int receipt = 0;
    for (int i = 0; i < N; ++i) {
        int a;
        short b;

        cin >> a >> b;

        receipt += a * b;
    }

    if (receipt == X) {
        cout << "Yes" << endl;
    } else {
        cout << "No" << endl;
    }

    return 0;
}
