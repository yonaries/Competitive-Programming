n, k = map(int, input().split())
 
seq = sorted(map(int, input().split()))
 
if k == n and seq[k - 1] <= 10 ** 9:
    print(seq[k - 1])
elif seq[k - 1] == 10 ** 9:
    print(seq[k - 1])
elif k == 0 and seq[0] > 1:
    print(seq[0] -  1)
elif 0 < k < n and seq[k - 1] != seq[k]:
    print(seq[k - 1])
else:
    print(-1)
