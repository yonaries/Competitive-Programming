from collections import deque

n = int(input())
t = list(map(int, input().split()))
t.sort()

queue = deque()

total_time_taken = 0
total_disappointed_people = 0

for time in t:
    queue.append(time)
    total_time_taken += time

    if total_time_taken > time:
        total_disappointed_people += 1
        queue.popleft()

print(total_disappointed_people)
