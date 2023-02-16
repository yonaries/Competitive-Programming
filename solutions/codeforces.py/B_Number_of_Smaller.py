

def smallerNumbers(n, m, arr1, arr2):
    output = []
    for i in range(m):
        count = 0
        for j in range(n):
            if arr1[j] < arr2[i]:
                count += 1
            else:
                break
        output.append(str(count))
    return ' '.join(output)


n, m = list(map(int, input().split()))
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

print(smallerNumbers(n, m, arr1, arr2))
