#include <iostream>
#include <vector>

using namespace std;

int main() {
    int N, M;
    cin >> N >> M;

    vector<int> basket(N);
    for (int i = 0; i < N; ++i) {
        basket[i] = i + 1;
    }

    for (int x = 0; x < M; ++x) {
        int a, b;
        cin >> a >> b;

        int temp = basket[a - 1];
        basket[a - 1] = basket[b - 1];
        basket[b - 1] = temp;
    }

    for (auto item: basket) {
        cout << item << " ";
    }

    return 0;
}