#include <iostream>
using namespace std;

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        int xor_all = 0, xor_except_last = 0;
        for (int i = 0; i < n; i++) {
            int a;
            cin >> a;
            xor_all ^= a;
            if (i < n-1) {
                xor_except_last ^= a;
            }
        }
        cout << (xor_all ^ xor_except_last) << endl;
    }
    return 0;
}
