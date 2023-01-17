def minimum_light_radius(n, l, lanterns):
    lanterns.sort()
    max_distance = 0
    for i in range(n):
        if i == 0:
            max_distance = max(max_distance, lanterns[i])
        elif i == n-1:
            max_distance = max(max_distance, l-lanterns[i])
        else:
            max_distance = max(max_distance, (lanterns[i+1]-lanterns[i-1])/2)
    return max_distance


n, l = map(int, input().split())
lanterns = list(map(int, input().split()))
print(minimum_light_radius(n, l, lanterns))
