#include <iostream>
#include <vector>

using namespace std;

int main() {
    short N, M;
    cin >> N >> M;

    vector<int> basket(N, 0);

    for (int x = 0; x < M; ++x) {
        int i, j, k;
        cin >> i >> j >> k;

        for (int y = i - 1; y < j; ++y) {
            basket[y] = k;
        }
    }

    for (auto item: basket) {
        cout << item << " ";
    }

    return 0;
}
