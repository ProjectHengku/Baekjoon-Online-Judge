#include <stdio.h>
#include <iostream>

using namespace std;

int main() {
    int testCase;
    cin >> testCase;

    for (int i = 1; i <= testCase; i++)
    {
        int A, B;
        cin >> A >> B;

        cout << "Case #" << i << ": " << A << " + " << B << " = " << A + B << endl;
    }
    return 0;
}