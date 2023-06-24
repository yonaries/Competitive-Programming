n, k = list(map(int, input().split()))
a = list(map(int, input().split()))

# do a suffix sum on the array
suffixSum = [a[-1]]
for i in range(n-2, 0, -1):
    suffixSum.append(suffixSum[-1] + a[i])

suffixSum.sort(reverse=True)
result = sum(a)

# sum the first k-1 elements of the suffix sum which are the largest sums
for i in range(k-1):
    result += suffixSum[i]
print(result)
