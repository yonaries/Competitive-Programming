a = list(map(int, input()))
b = list(map(int, input()))

result = []

for i in range(len(a)):
    if a[i] ^ b[i]:
        result.append(1)
    else:
        result.append(0)
        
print(*result, sep='')