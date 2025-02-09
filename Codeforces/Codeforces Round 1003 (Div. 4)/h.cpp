#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
const ll MODULO = 998244353;

struct FenwickTree
{
    int sz;
    vector<ll> tree;
    FenwickTree(int size) : sz(size) { tree.assign(size + 1, 0); }

    void update(int idx, ll delta)
    {
        for (; idx <= sz; idx += idx & -idx)
        {
            tree[idx] = (tree[idx] + delta) % MODULO;
            if (tree[idx] < 0)
                tree[idx] += MODULO;
        }
    }

    ll query(int idx)
    {
        ll sum = 0;
        for (; idx; idx -= idx & -idx)
            sum = (sum + tree[idx]) % MODULO;
        return sum;
    }

    ll rangeQuery(int left, int right)
    {
        if (left > right)
            return 0;
        return (query(right) - query(left - 1) + MODULO) % MODULO;
    }
};

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int testCases;
    cin >> testCases;
    const int MAXN = 200005;

    vector<ll> power2(MAXN);
    power2[0] = 1;
    for (int i = 1; i < MAXN; i++)
        power2[i] = (power2[i - 1] * 2) % MODULO;

    while (testCases--)
    {
        string binaryString;
        cin >> binaryString;
        int len = binaryString.size();
        int queries;
        cin >> queries;

        FenwickTree FT0(len), FT1(len), IT0(len), IT1(len);
        ll result = 0, count0 = 0, count1 = 0;

        for (int i = 1; i <= len; i++)
        {
            if (binaryString[i - 1] == '0')
            {
                result = (result + count1 * power2[len - i]) % MODULO;
                count0 = (count0 + power2[i - 1]) % MODULO;
                FT0.update(i, power2[i - 1]);
                IT0.update(i, power2[len - i]);
            }
            else
            {
                result = (result + count0 * power2[len - i]) % MODULO;
                count1 = (count1 + power2[i - 1]) % MODULO;
                FT1.update(i, power2[i - 1]);
                IT1.update(i, power2[len - i]);
            }
        }

        for (int i = 0; i < queries; i++)
        {
            int idx;
            cin >> idx;
            int curr = binaryString[idx - 1] - '0', next = 1 - curr;

            ll sum1 = (curr == 0 ? IT0.rangeQuery(idx + 1, len) : IT1.rangeQuery(idx + 1, len));
            ll sum2 = (next == 0 ? IT0.rangeQuery(idx + 1, len) : IT1.rangeQuery(idx + 1, len));
            ll diff1 = (power2[idx - 1] * ((sum1 - sum2) % MODULO)) % MODULO;
            if (diff1 < 0)
                diff1 += MODULO;

            ll sum3 = (curr == 0 ? FT0.rangeQuery(1, idx - 1) : FT1.rangeQuery(1, idx - 1));
            ll sum4 = (next == 0 ? FT0.rangeQuery(1, idx - 1) : FT1.rangeQuery(1, idx - 1));
            ll diff2 = (power2[len - idx] * ((sum3 - sum4) % MODULO)) % MODULO;
            if (diff2 < 0)
                diff2 += MODULO;

            ll totalDiff = (diff1 + diff2) % MODULO;
            result = (result + totalDiff) % MODULO;

            if (curr == 0)
            {
                FT0.update(idx, -power2[idx - 1]);
                IT0.update(idx, -power2[len - idx]);
            }
            else
            {
                FT1.update(idx, -power2[idx - 1]);
                IT1.update(idx, -power2[len - idx]);
            }
            if (next == 0)
            {
                FT0.update(idx, power2[idx - 1]);
                IT0.update(idx, power2[len - idx]);
            }
            else
            {
                FT1.update(idx, power2[idx - 1]);
                IT1.update(idx, power2[len - idx]);
            }

            binaryString[idx - 1] = char('0' + next);
            ll finalRes = (power2[len] - 1 + result) % MODULO;
            if (finalRes < 0)
                finalRes += MODULO;
            cout << finalRes << " ";
        }
        cout << "\n";
    }
    return 0;
}
