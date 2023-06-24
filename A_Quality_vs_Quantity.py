def solve(sequence, n):
    sequence.sort()

    for i in range(n-1, -1, -1):
        if sum(sequence[:i]) < sum(sequence[i:]) and len(sequence[:i]) > len(sequence[i:]):
            return "YES"

    return "NO"


tests = int(input())
for _ in range(tests):
    n = int(input())
    sequence = list(map(int, input().split()))
    print(solve(sequence, n))
