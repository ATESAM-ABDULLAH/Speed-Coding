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
        int n;
        cin >> n;

        vector<int> a(n + 1);
        for (int i = 1; i <= n; i++)
        {
            cin >> a[i];
        }

        vector<vector<int>> g(n + 1);
        for (int i = 1; i < n; i++)
        {
            int u, v;
            cin >> u >> v;
            g[u].push_back(v);
            g[v].push_back(u);
        }

        vector<char> ans(n + 1, '0');
        for (int i = 1; i <= n; i++)
        {
            for (auto j : g[i])
            {
                if (a[i] == a[j])
                {
                    ans[a[i]] = '1';
                }
            }
        }

        for (int i = 1; i <= n; i++)
        {
            if (g[i].empty())
                continue;

            vector<int> tmp;
            tmp.reserve(g[i].size());

            for (auto j : g[i])
            {
                tmp.push_back(a[j]);
            }

            sort(tmp.begin(), tmp.end());

            int cnt = 1;
            for (int k = 1; k < tmp.size(); k++)
            {
                if (tmp[k] == tmp[k - 1])
                {
                    cnt++;
                    if (cnt >= 2)
                    {
                        ans[tmp[k]] = '1';
                    }
                }
                else
                {
                    cnt = 1;
                }
            }
        }

        string s;
        s.resize(n);
        for (int i = 1; i <= n; i++)
        {
            s[i - 1] = ans[i];
        }

        cout << s << "\n";
    }

    return 0;
}
