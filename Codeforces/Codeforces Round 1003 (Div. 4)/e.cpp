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
        int n, m, k;
        cin >> n >> m >> k;
        string s;
        s.reserve(n + m);
        if (n >= m)
        {
            if (k < n - m || k > n)
            {
                cout << -1 << "\n";
                continue;
            }
            for (int i = 0; i < k; i++)
                s.push_back('0');
            int ru = n - k, rd = m, cur = k, T = n - m;
            while (ru + rd)
            {
                if (cur == k)
                {
                    s.push_back('1');
                    cur--;
                    rd--;
                }
                else if (cur == 0)
                {
                    s.push_back('0');
                    cur++;
                    ru--;
                }
                else
                {
                    int d = T - cur;
                    if (d > 0)
                    {
                        if (ru && cur < k)
                        {
                            s.push_back('0');
                            cur++;
                            ru--;
                        }
                        else
                        {
                            s.push_back('1');
                            cur--;
                            rd--;
                        }
                    }
                    else if (d < 0)
                    {
                        if (rd && cur > 0)
                        {
                            s.push_back('1');
                            cur--;
                            rd--;
                        }
                        else
                        {
                            s.push_back('0');
                            cur++;
                            ru--;
                        }
                    }
                    else
                    {
                        if (ru >= rd && cur < k)
                        {
                            s.push_back('0');
                            cur++;
                            ru--;
                        }
                        else
                        {
                            s.push_back('1');
                            cur--;
                            rd--;
                        }
                    }
                }
            }
            if ((int)s.size() != n + m)
                cout << -1 << "\n";
            else
                cout << s << "\n";
        }
        else
        {
            if (k < m - n || k > m)
            {
                cout << -1 << "\n";
                continue;
            }
            for (int i = 0; i < k; i++)
                s.push_back('1');
            int ru = m - k, rd = n, cur = k, T = m - n;
            while (ru + rd)
            {
                if (cur == k)
                {
                    s.push_back('0');
                    cur--;
                    rd--;
                }
                else if (cur == 0)
                {
                    s.push_back('1');
                    cur++;
                    ru--;
                }
                else
                {
                    int d = T - cur;
                    if (d > 0)
                    {
                        if (ru && cur < k)
                        {
                            s.push_back('1');
                            cur++;
                            ru--;
                        }
                        else
                        {
                            s.push_back('0');
                            cur--;
                            rd--;
                        }
                    }
                    else if (d < 0)
                    {
                        if (rd && cur > 0)
                        {
                            s.push_back('0');
                            cur--;
                            rd--;
                        }
                        else
                        {
                            s.push_back('1');
                            cur++;
                            ru--;
                        }
                    }
                    else
                    {
                        if (ru >= rd && cur < k)
                        {
                            s.push_back('1');
                            cur++;
                            ru--;
                        }
                        else
                        {
                            s.push_back('0');
                            cur--;
                            rd--;
                        }
                    }
                }
            }
            if ((int)s.size() != n + m)
                cout << -1 << "\n";
            else
                cout << s << "\n";
        }
    }
    return 0;
}