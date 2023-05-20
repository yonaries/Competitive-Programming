def dfs(x, b, steps):
    if x == b:
        print("YES")
        print(len(steps))
        print(*steps)
        return True

    if x > b:
        return False

    steps.append(x * 2)

    if dfs(x * 2, b, steps):
        return True

    steps.pop()
    steps.append(x * 10 + 1)

    if dfs(x * 10 + 1, b, steps):
        return True

    steps.pop()
    return False


a, b = map(int, input().split())
if not dfs(a, b, [a]):
    print("NO")
