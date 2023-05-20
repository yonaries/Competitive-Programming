length_of_stone_prices = int(input())
price = list(map(int, input().split()))
price_sorted = price.copy()
price_sorted.sort()

m = int(input())
for i in range(m):
    original_sum = 0
    sorted_sum = 0
    typeof, left, right = list(map(int, input().split()))

    for i in range(left - 1, right):
        original_sum += price[i]
        sorted_sum += price_sorted[i]

    if typeof == 1:
        print(original_sum)
    else:
        print(sorted_sum)
