def possibleTriangle(lines):
    for i in range(0, len(lines)-2):
        if (lines[i] + lines[i + 1] > lines[i + 2]):
            return 'YES'
    return 'NO'


size = int(input())
lines = list(map(int, input().split()))
lines.sort()
print(possibleTriangle(lines))
