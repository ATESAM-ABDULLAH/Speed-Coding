#include <bits/stdc++.h>
using namespace std;
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while (t--)
    {
        int n, m;
        cin >> n >> m;
        vector<int> a(n);
        for (auto &x : a)
            cin >> x;
        vector<long long> b(m);
        for (auto &x : b)
            cin >> x;
        sort(b.begin(), b.end());

        const long long INF = 1e18;
        long long dp = -1e18;
        bool ok = true;
        for (int i = 0; i < n; i++)
        {
            long long ai = a[i];
            long long op0 = INF, op1 = INF;
            if (ai >= dp)
                op0 = ai;
            long long need = dp + ai;
            auto it = lower_bound(b.begin(), b.end(), need);
            if (it != b.end())
            {
                op1 = (*it) - ai;
            }
            long long cur = min(op0, op1);
            if (cur == INF)
            {
                ok = false;
                break;
            }
            dp = cur;
        }
        cout << (ok ? "YES" : "NO") << "\n";
    }
    return 0;
}
