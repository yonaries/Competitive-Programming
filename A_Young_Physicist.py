n = int(input())


def young_physicist(arr, length):
    x = 0
    y = 0
    z = 0
    for i in range(length):
        x += arr[i][0]
        y += arr[i][1]
        z += arr[i][2]
    if x == 0 and y == 0 and z == 0:
        return "YES"
    else:
        return "NO"


arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
print(young_physicist(arr, n))
