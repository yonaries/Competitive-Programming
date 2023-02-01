set_1 = set(input().split())
strict = True
for i in range(int(input())):
    inner_set = set(input().split())
    if inner_set.issubset(set_1) and len(set_1 - inner_set) >= 1:
        pass
    else:
        strict = False
        break
print(strict)  