from collections import defaultdict


def dfs(graph, visited, v):
    visited[v] = True
    for u in graph[v]:
        if not visited[u]:
            dfs(graph, visited, u)


def is_valid(n, m, edges):
    # Build the graph
    graph = defaultdict(list)
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    # Check property 1
    visited = [False] * (n + 1)
    dfs(graph, visited, 1)
    if False in visited[1:]:
        return "no"

    # Check property 2
    bridges = 0
    visited = [False] * (n + 1)
    low = [0] * (n + 1)
    disc = [0] * (n + 1)
    parent = [-1] * (n + 1)

    def bridge_dfs(v):
        nonlocal bridges
        visited[v] = True
        low[v] = disc[v] = bridge_dfs.time
        bridge_dfs.time += 1
        for u in graph[v]:
            if not visited[u]:
                parent[u] = v
                bridge_dfs(u)
                low[v] = min(low[v], low[u])
                if low[u] > disc[v]:
                    bridges += 1
            elif u != parent[v]:
                low[v] = min(low[v], disc[u])

    bridge_dfs.time = 0
    bridge_dfs(1)
    if bridges > 0:
        return "no"

    return "yes"


n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
print(is_valid(n, m, edges))
