from collections import deque

n, m = map(int, input().split())

queue = deque([(n, 0)])
visited = set([n])

while queue:
    num, clicks = queue.popleft()

    if num == m:
        print(clicks)
        break

    if num*2 not in visited and num*2 > 0:
        queue.append((num*2, clicks+1))
        visited.add(num*2)

    if num-1 not in visited and num-1 > 0:
        queue.append((num-1, clicks+1))
        visited.add(num-1)
