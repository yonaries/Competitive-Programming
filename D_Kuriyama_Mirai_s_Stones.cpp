#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int length_of_stone_prices;
    cin >> length_of_stone_prices;

    vector<int> price(length_of_stone_prices);
    for (int i = 0; i < length_of_stone_prices; i++) {
        cin >> price[i];
    }

    vector<int> price_sorted = price;
    sort(price_sorted.begin(), price_sorted.end());

    int m;
    cin >> m;

    for (int i = 0; i < m; i++) {
        int original_sum = 0;
        int sorted_sum = 0;
        int typeof_stone, left, right;
        cin >> typeof_stone >> left >> right;

        for (int j = left - 1; j < right; j++) {
            original_sum += price[j];
            sorted_sum += price_sorted[j];
        }

        if (typeof_stone == 1) {
            cout << original_sum << endl;
        } else {
            cout << sorted_sum << endl;
        }
    }

    return 0;
}
