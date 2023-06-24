#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int solve()
{
    int n;
    cin >> n;
    vector<ll> a(n);
    for (int i = 0; i < n; i++)
    {
        cin >> a[i];
    }
    cout << n << endl;
    for (int i = 0; i < n; i++)
    {
        ll deg = 1;
        while (deg < a[i])
        {
            deg *= 2;
        }
        cout << i + 1 << ' ' << deg - a[i] << endl;
    }
    return 0;
}
int main()
{
    long long testCase;
    cin >> testCase;
    while (testCase--)
    {
        solve();
    }
    return 0;
}