n = int(input())
adj_matrix = []
for i in range(n):
    row = list(map(int, input().split()))
    adj_matrix.append(row)

adj_list = [[] for i in range(n)]
for i in range(n):
    for j in range(n):
        if adj_matrix[i][j] == 1:
            adj_list[i].append(j+1)

for i in range(n):
    print(len(adj_list[i]), end=' ')
    for j in range(len(adj_list[i])):
        print(adj_list[i][j], end=' ')
    print()
