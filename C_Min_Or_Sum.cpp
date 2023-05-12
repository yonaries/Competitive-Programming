#include <bits/stdc++.h>
using namespace std;

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        vector<int> a(n);
        for (int i = 0; i < n; i++) {
            cin >> a[i];
        }
        int min_or = INT_MAX;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                min_or = min(min_or, a[i] | a[j]);
            }
        }
        long long sum = 0;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if ((a[i] | a[j]) == min_or) {
                    int x = a[i], y = a[j];
                    while ((x | y) == min_or) {
                        x /= 2;
                        y /= 2;
                    }
                    sum += x + y;
                    a[i] = x;
                    a[j] = y;
                }
            }
        }
        for (int i = 0; i < n; i++) {
            sum += a[i];
        }
        cout << sum << endl;
    }
    return 0;
}
