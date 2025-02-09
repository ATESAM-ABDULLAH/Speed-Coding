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

        vector<long long> a(n), b(m);
        for (auto &x : a)
            cin >> x;
        for (auto &x : b)
            cin >> x;

        sort(b.begin(), b.end());

        const long long INF = 1LL << 60;
        long long dp = -INF;
        bool ok = true;

        for (int i = 0; i < n; i++)
        {
            long long o1 = INF, o2 = INF;

            if (a[i] >= dp)
                o1 = a[i];

            long long T = dp + a[i];
            auto it = lower_bound(b.begin(), b.end(), T);

            if (it != b.end())
                o2 = *it - a[i];

            long long cur = min(o1, o2);
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
