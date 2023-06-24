#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

int main() {
    int n;
    cin >> n;

    vector<int> widths(n);
    for (int i = 0; i < n; i++) {
        cin >> widths[i];
    }

    vector<int> persons(2 * n);
    for (int i = 0; i < 2 * n; i++) {
        cin >> persons[i];
    }

    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> minHeap;
    priority_queue<pair<int, int>, vector<pair<int, int>>, less<pair<int, int>>> maxHeap;

    // build min heap to assign sets to introverts
    for (int i = 0; i < n; i++) {
        minHeap.push(make_pair(widths[i], i + 1));
    }

    vector<int> seats;
    for (int i = 0; i < 2 * n; i++) {
        if (persons[i] == 0) {
            pair<int, int> minTop = minHeap.top();
            minHeap.pop();
            seats.push_back(minTop.second);
            maxHeap.push(make_pair(minTop.first, minTop.second));
        } else {
            pair<int, int> maxTop = maxHeap.top();
            maxHeap.pop();
            seats.push_back(maxTop.second);
        }
    }

    for (int i = 0; i < seats.size(); i++) {
        cout << seats[i] << " ";
    }

    return 0;
}
