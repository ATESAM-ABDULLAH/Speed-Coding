#include <bits/stdc++.h>
using namespace std;

const int MAX = 200000;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    vector<bool> ip(MAX + 1, true);
    ip[0] = ip[1] = false;
    for (int i = 2; i * i <= MAX; i++)
        if (ip[i])
            for (int j = i * i; j <= MAX; j += i)
                ip[j] = false;

    vector<int> spf(MAX + 1);
    for (int i = 0; i <= MAX; i++)
        spf[i] = i;
    for (int i = 2; i * i <= MAX; i++)
        if (spf[i] == i)
            for (int j = i * i; j <= MAX; j += i)
                if (spf[j] == j)
                    spf[j] = i;

    int t;
    cin >> t;
    while (t--)
    {
        int n;
        cin >> n;
        vector<int> f(n + 1, 0);
        for (int i = 0; i < n; i++)
        {
            int x;
            cin >> x;
            if (x <= n)
                f[x]++;
        }

        vector<long long> A(n + 1, 0), B(n + 1, 0);
        unordered_map<unsigned long long, long long> C;
        C.reserve(n);
        vector<bool> use(n + 1, false);

        for (int x = 2; x <= n; x++)
        {
            if (!f[x])
                continue;
            if (ip[x])
            {
                A[x] += f[x];
                use[x] = true;
            }
            else
            {
                int p = spf[x], r = x / p;
                if (r >= 2 && ip[r])
                {
                    if (p == r)
                    {
                        B[p] += f[x];
                        use[p] = true;
                    }
                    else
                    {
                        int a = min(p, r), b = max(p, r);
                        unsigned long long key = ((unsigned long long)a << 32) | (unsigned int)b;
                        C[key] += f[x];
                        use[a] = use[b] = true;
                    }
                }
            }
        }

        vector<int> P;
        long long s = 0, sq = 0;
        for (int i = 2; i <= n; i++)
            if (use[i] && ip[i])
            {
                P.push_back(i);
                s += A[i];
                sq += A[i] * A[i];
            }

        long long ans = 0;
        for (auto p : P)
            if ((long long)p * p <= n)
                ans += A[p] * B[p] + (B[p] * (B[p] - 1LL)) / 2 + B[p];

        ans += (s * s - sq) / 2;

        for (auto &it : C)
        {
            unsigned long long key = it.first;
            long long cnt = it.second;
            int a = key >> 32, b = key & 0xffffffffULL;
            ans += (A[a] + A[b]) * cnt + (cnt * (cnt - 1LL)) / 2 + cnt;
        }

        cout << ans << "\n";
    }

    return 0;
}
