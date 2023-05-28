n, d = map(int, input().split())
s = input()

pos, jumps = 0, 0
while pos < n - 1:
    found = False
    for i in range(min(n - 1, pos + d), pos, -1):
        if s[i] == '1':
            pos = i
            jumps += 1
            found = True
            break
    if not found:
        print(-1)
        exit()

print(jumps)
