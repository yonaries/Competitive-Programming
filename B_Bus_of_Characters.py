from heapq import heappush, heappop, _heapify_max

n = int(input())
widths = list(map(int, input().split()))
persons = list(map(int, input().strip()))

min_heap = []
max_heap = []

# build min heap to assign sets to introverts
for i in range(n):
    heappush(min_heap, (widths[i], i+1))

seats = []
for i in range(2*n):
    if persons[i] == 0:
        width, index = heappop(min_heap)
        seats.append(index)
        heappush(max_heap, (width, index))

    else:
        _heapify_max(max_heap)
        width, index = heappop(max_heap)
        seats.append(index)

print(*seats)
