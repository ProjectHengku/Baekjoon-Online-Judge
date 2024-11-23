#include <iostream>

int main() {
    double A, B;

    std::cin >> A >> B;

    double result = A / B;
    std::cout.precision(10);
    std::cout << result << std::endl;
    return 0;
}