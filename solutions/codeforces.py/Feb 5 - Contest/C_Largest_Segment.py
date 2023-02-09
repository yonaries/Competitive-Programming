import math
n = int(input())
coordinates = []

for _ in range(n):
    coordinates.append(list(map(int, input().split(' '))))


def largestSegment(coordinates: list[list]) -> int:
    start = math.inf
    end = -math.inf

    for coordinate in coordinates:
        start = min(start, coordinate[0])
        end = max(end, coordinate[1])

    largest = [start, end]

    for i in range(len(coordinates)):
        if coordinates[i] == largest:
            return i+1

    return -1


result = largestSegment(coordinates)
print(result)
