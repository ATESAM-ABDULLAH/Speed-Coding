#include <iostream>
#include <vector>
#include <queue>
#include <climits>
using namespace std;

#define INF 1e9
#define pii pair<int, int>
#define pd pair<double, int>
#define vi vector<int>
#define vpi vector<pii>
#define vd vector<double>
#define pb push_back
#define F first
#define S second
#define all(x) (x).begin(), (x).end()


vd dijkstra(int n, vector<vpi>& graph, int start)
{
    vd dist(n + 1, INF);
    dist[start] = 0;
    priority_queue<pii, vector<pii>, greater<pii>> pq;
    pq.push({0, start});

    while (!pq.empty())
    {
        double d = pq.top().F;
        int u = pq.top().S;
        pq.pop();

        if (d > dist[u]) continue;

        for (auto& edge : graph[u])
        {
            int v = edge.F;
            double weight = edge.S;
            if (dist[u] + weight < dist[v])
            {
                dist[v] = dist[u] + weight;
                pq.push({dist[v], v});
            }
        }
    }

    return dist;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    int t;
    cin >> t;

    while (t--)
    {
        int n, m;
        cin >> n >> m;

        vector<vpi> graph(n + 1);

        for (int i = 0; i < m; ++i)
        {
            int u, v;
            double d;
            cin >> u >> v >> d;
            graph[u].pb({v, d});
            graph[v].pb({u, d});
        }

        pd best = {INF, -1};

        for (int i = 1; i <= n; ++i)
        {
            vd dist = dijkstra(n, graph, i);
            double total = 0;
            for (int j = 1; j <= n; ++j)
            {
                if (i != j)
                {
                    total += dist[j];
                }
            }
            double avg = total / (n - 1);

            if (avg < best.F || (avg == best.F && i < best.S))
            {
                best.F = avg;
                best.S = i;
            }
        }

        cout << best.S << "\n";
    }
}