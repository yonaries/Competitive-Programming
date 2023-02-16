n_testcases = int(input())


def polycarpSequence(sequence, length):
    output = [0 for _ in range(length)]
    left = 0
    right = length-1

    for i in range(length):
        if (i % 2 == 0 and output[i] == 0):
            output[i] = str(sequence[left])
            left += 1
        elif (i % 2 != 0 and output[i] == 0):
            output[i] = str(sequence[right])
            right -= 1
    return ' '.join(output)


for _ in range(n_testcases):
    length = int(input())
    sequence = list(map(int, input().split()))
    result = polycarpSequence(sequence, length)
    print(result)

# result = polycarpSequence([3, 4, 5, 2, 9, 1, 1], 7)
# print(result)
