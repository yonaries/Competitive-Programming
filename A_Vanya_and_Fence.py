n, h = list(map(int, input().split()))
boys = list(map(int, input().split()))

count = 0
for height in boys:
    if height > h:
        count += 2
    else:
        count += 1
print(count)
