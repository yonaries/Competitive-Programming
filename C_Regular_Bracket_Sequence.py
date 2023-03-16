s = input().strip()
stack = []
count = 0

for c in s:
    if c == '(':
        stack.append(c)
    elif stack:
        stack.pop()
        count += 2

print(count)
