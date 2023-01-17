from collections import defaultdict
n, m = map(int, input().split(' '))

dic = defaultdict(list)

# tracking indices of characters in groupA
for i in range(n):
    ch = input()
    dic[ch].append(str(i + 1))

for i in range(m):
    ch = input()
    if ch in dic:
        print(' '.join(dic[ch]))
    else:
        print(-1)
