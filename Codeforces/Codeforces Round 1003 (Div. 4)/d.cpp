#include <bits/stdc++.h>
using namespace std;

struct Arr
{
    long long tot, scr;
};

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
        vector<Arr> a(n);
        for (int i = 0; i < n; i++)
        {
            long long tot = 0, scr = 0, cur = 0;
            for (int j = 0; j < m; j++)
            {
                int x;
                cin >> x;
                cur += x;
                tot += x;
                scr += cur;
            }
            a[i] = {tot, scr};
        }
        sort(a.begin(), a.end(), [](const Arr &A, const Arr &B)
             { return A.tot > B.tot; });

        long long ans = 0;
        for (auto &x : a)
            ans += x.scr;
        for (int i = 0; i < n; i++)
        {
            ans += (long long)m * a[i].tot * (n - 1 - i);
        }

        cout << ans << "\n";
    }
    return 0;
}
