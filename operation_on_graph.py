n = int(input())
k = int(input())

adj_list = [[] for i in range(n+1)]

for i in range(k):
    op = list(map(int, input().split()))
    if op[0] == 1:
        u, v = op[1], op[2]
        adj_list[u].append(v)
        adj_list[v].append(u)
        
    elif op[0] == 2:
        u = op[1]
        for v in adj_list[u]:
            print(v, end=' ')
        print()
