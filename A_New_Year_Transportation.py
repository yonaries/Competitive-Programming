import sys
import threading


def input(): return sys.stdin.readline().strip()


def main():
    # My solution
    n, t = map(int, input().split())
    a = list(map(int, input().split()))

    # Build the port graph
    ports = [[] for _ in range(n)]
    for i in range(n-1):
        ports[i].append(i + a[i])

    visited = set()

    # DFS traversal
    def dfs(node, ports, target):
        if node == target:
            return True
        visited.add(node)
        for neighbor in ports[node]:
            if neighbor not in visited:
                if dfs(neighbor, ports, target):
                    return True
        return False

    if dfs(0, ports, t-1):
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
