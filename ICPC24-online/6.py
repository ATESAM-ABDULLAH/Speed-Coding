from collections import defaultdict, deque


def bfs(graph, root):
    queue = deque([(root, 1)])
    visited = set()
    max_depth = 0

    while queue:
        node, depth = queue.popleft()
        visited.add(node)
        max_depth = max(max_depth, depth)
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append((neighbor, depth + 1))

    return max_depth


def find_connected_trees(graph):
    degrees = defaultdict(int)
    for node, neighbors in graph.items():
        degrees[node] = len(neighbors)

    sorted_degrees = sorted(degrees.items(), key=lambda x: x[1], reverse=True)
    return sorted_degrees[0][1], sorted_degrees[1][1]


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        graph = defaultdict(list)
        for _ in range(n - 1):
            u, v = map(int, input().split())
            graph[u].append(v)
            graph[v].append(u)

        depth = bfs(graph, 0)
        connected_trees = find_connected_trees(graph)

        print(depth, connected_trees[0], connected_trees[1])


if __name__ == "__main__":
    main()
