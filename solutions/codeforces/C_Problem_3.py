size = int(input())
coins = list(map(int, input().split()))
coins.sort(reverse=True)

half = sum(coins)/2
mine = 0
count = 0

while mine <= half:
    mine += coins[count]
    count += 1

print(count)
