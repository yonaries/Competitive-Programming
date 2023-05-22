

import sys
import threading


def input(): return sys.stdin.readline().strip()


def main():
    n, m = list(map(int, input().split()))
    characters = list(map(int, input().split()))
    adjacency = [[] for _ in range(n)]

    # constructing adjacency list for the connected components
    for _ in range(m):
        a, b = list(map(int, input().split()))
        adjacency[a-1].append(b-1)
        adjacency[b-1].append(a-1)

    print(adjacency)

    # dfs to visit all nodes in a connected component
    def dfs(v):
        min_gold = characters[v]
        visited.add(v)
        for i in adjacency[v]:
            if i not in visited:
                min_gold = min(min_gold, dfs(i))

        return min_gold

    visited = set()
    golds = 0

    # traversing all connected components
    for i in range(n):
        if i not in visited:
            golds += dfs(i)

    print(golds)


if __name__ == '__main__':
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
