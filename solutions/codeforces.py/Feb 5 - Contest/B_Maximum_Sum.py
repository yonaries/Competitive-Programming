n, m = list(map(int, input().split(' ')))
prices = list(map(int, input().split(' ')))
prices.sort()

earnings = 0

for i in range(m):
    if prices[i] < 0:
        earnings += abs(prices[i])

print(earnings)
