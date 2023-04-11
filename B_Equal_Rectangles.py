from collections import Counter


def construct_rectangle(sticks: list):
    i = 0
    j = 1

    stick = []

    sticks.sort()
    while j <= len(sticks):
        if sticks[i] == sticks[j]:
            stick.append(sticks[i])
            i += 2
            j += 2

        else:
            i += 1
            j += 1
    print(stick)
    areas = []
    for i in range(len(stick)):
        for j in range(i+1, len(stick)):
            areas.append(stick[i] * stick[j])
    max_count = max(Counter(areas).values())
    return max_count


if __name__ == '__main__':
    testcase_length = int(input())

    for _ in range(testcase_length):
        n = int(input())
        sticks = list(map(int, input().split()))

        if n == construct_rectangle(sticks):
            print('YES')
        else:
            print('NO')
