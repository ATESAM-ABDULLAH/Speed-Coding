#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    int t;
    cin >> t;

    while (t--)
    {
        int n, m;
        cin >> n >> m;

        vector<long long> A(n);
        for (auto &i : A)
            cin >> i;

        long long x;
        cin >> x;

        bool c[2] = {true, true};

        for (int i = 1; i < n; i++)
        {
            bool d[2] = {false, false};

            for (int j = 0; j < 2; j++)
            {
                if (!c[j])
                    continue;

                long long p = j ? x - A[i - 1] : A[i - 1];

                for (int k = 0; k < 2; k++)
                {
                    long long q = k ? x - A[i] : A[i];
                    if (p <= q)
                        d[k] = true;
                }
            }

            c[0] = d[0], c[1] = d[1];
        }

        cout << (c[0] || c[1] ? "YES" : "NO") << "\n";
    }

    return 0;
}
