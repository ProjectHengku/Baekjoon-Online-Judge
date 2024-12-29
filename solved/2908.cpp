#include <iostream>
#include <algorithm>

int main() {
    std::string A, B;

    std::cin >> A >> B;

    std::reverse(A.begin(), A.end());
    std::reverse(B.begin(), B.end());

    std::cout << std::max(std::stoi(A), std::stoi(B)) << std::endl;

    return 0;
}