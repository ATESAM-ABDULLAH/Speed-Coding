#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
const ll MOD = 998244353;

struct BIT
{
    int n;
    vector<ll> f;
    BIT(int n) : n(n) { f.assign(n + 1, 0); }
    void upd(int i, ll d)
    {
        for (; i <= n; i += i & -i)
        {
            f[i] = (f[i] + d) % MOD;
            if (f[i] < 0)
                f[i] += MOD;
        }
    }
    ll qry(int i)
    {
        ll s = 0;
        for (; i; i -= i & -i)
            s = (s + f[i]) % MOD;
        return s;
    }
    ll rng(int l, int r)
    {
        if (l > r)
            return 0;
        return (qry(r) - qry(l - 1) + MOD) % MOD;
    }
};

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    const int MAX = 200005;
    vector<ll> p(MAX);
    p[0] = 1;
    for (int i = 1; i < MAX; i++)
        p[i] = (p[i - 1] * 2) % MOD;

    while (T--)
    {
        string s;
        cin >> s;
        int n = s.size();
        int q;
        cin >> q;
        BIT b0(n), b1(n), a0(n), a1(n);
        ll F = 0, r0 = 0, r1 = 0;
        for (int i = 1; i <= n; i++)
        {
            if (s[i - 1] == '0')
            {
                F = (F + r1 * p[n - i]) % MOD;
                r0 = (r0 + p[i - 1]) % MOD;
                b0.upd(i, p[i - 1]);
                a0.upd(i, p[n - i]);
            }
            else
            {
                F = (F + r0 * p[n - i]) % MOD;
                r1 = (r1 + p[i - 1]) % MOD;
                b1.upd(i, p[i - 1]);
                a1.upd(i, p[n - i]);
            }
        }
        for (int i = 0; i < q; i++)
        {
            int k;
            cin >> k;
            int o = s[k - 1] - '0', w = 1 - o;
            ll S = (o == 0 ? a0.rng(k + 1, n) : a1.rng(k + 1, n));
            ll T = (w == 0 ? a0.rng(k + 1, n) : a1.rng(k + 1, n));
            ll d1 = (p[k - 1] * ((S - T) % MOD)) % MOD;
            if (d1 < 0)
                d1 += MOD;
            ll X = (o == 0 ? b0.rng(1, k - 1) : b1.rng(1, k - 1));
            ll Y = (w == 0 ? b0.rng(1, k - 1) : b1.rng(1, k - 1));
            ll d2 = (p[n - k] * ((X - Y) % MOD)) % MOD;
            if (d2 < 0)
                d2 += MOD;
            ll d = (d1 + d2) % MOD;
            F = (F + d) % MOD;
            if (o == 0)
            {
                b0.upd(k, -p[k - 1]);
                a0.upd(k, -p[n - k]);
            }
            else
            {
                b1.upd(k, -p[k - 1]);
                a1.upd(k, -p[n - k]);
            }
            if (w == 0)
            {
                b0.upd(k, p[k - 1]);
                a0.upd(k, p[n - k]);
            }
            else
            {
                b1.upd(k, p[k - 1]);
                a1.upd(k, p[n - k]);
            }
            s[k - 1] = char('0' + w);
            ll tot = (p[n] - 1 + F) % MOD;
            if (tot < 0)
                tot += MOD;
            cout << tot << " ";
        }
        cout << "\n";
    }
    return 0;
}
