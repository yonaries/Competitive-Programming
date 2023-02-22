length = int(input())


def ehab_is_odd(arr, length):
    for i in range(1, length):
        if arr[i] + arr[i-1] % 2 == 1:
            arr[i], arr[i-1] = arr[i-1], arr[i]
    return " ".join(map(str, arr))


arr = list(map(int, input().split()))
print(ehab_is_odd(arr, length))
