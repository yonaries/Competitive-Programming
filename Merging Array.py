if __name__ == '__main__':
    
    N, M = map(int, input().split())
    upper = list(map(int, input().split()))
    lower = list(map(int, input().split()))
 
    left = right = 0
    merged = []
 
    while left < len(upper) and right < len(lower):
        if upper[left] < lower[right]:
            merged.append(upper[left])
            left += 1
        else:
            merged.append(lower[right])
            right += 1
    
    while left < len(upper):
        merged.append(upper[left])
        left += 1
    
    while right < len(lower):
        merged.append(lower[right])
        right += 1
    
    print(*merged)
