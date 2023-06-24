import heapq


def solve():  # O((n+m)*logn)
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    b = list(map(int, input().split()))

    pq = []  # space: O(n)
    for num in arr:  # build the initial min heap. O(n*logn)
        heapq.heappush(pq, num)

    for j in range(m):  # O(m*logn)
        num = b[j]
        heapq.heappop(pq)  # remove the smallest element. O(logn)
        heapq.heappush(pq, num)  # add the new element from b. O(logn)

    _sum = sum(pq)  # O(n)
    print(_sum)


testCase = int(input())
while testCase > 0:
    solve()
    testCase -= 1
