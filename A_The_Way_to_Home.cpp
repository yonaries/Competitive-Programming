#include <iostream>
#include <string>

using namespace std;

int main() {
    int n, d;
    string s;
    cin >> n >> d >> s;

    int pos = 0 jumps = 0;
    while (pos < n - 1) {
        bool found = false;
        for (int i = min(n - 1, pos + d); i > pos; i--) {
            if (s[i] == '1') {
                pos = i;
                jumps++;
                found = true;
                break;
            }
        }
        if (!found) {
            cout << -1 << endl;
            return 0;
        }
    }

    cout << jumps << endl;
    return 0;
}
