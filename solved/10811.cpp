#include <iostream>
#include <vector>

int main() {
    int N, M;
    std::cin >> N >> M;

    std::vector<int> basket(N);
    for (int i = 0; i < N; ++i) {
        basket[i] = i + 1;
    }

    for (int x = 0; x < M; ++x) {
        int i, j;
        std::cin >> i >> j;

        std::vector<int> temp;
        for (int k = i - 1; k < j; ++k) {
            temp.push_back(basket[k]);
        }

        for (int l = 0; l < temp.size(); ++l) {
            basket[j - 1 - l] = temp[l];
        }
    }

    for (auto item: basket) {
        std::cout << item << " ";
    }

    return 0;
}