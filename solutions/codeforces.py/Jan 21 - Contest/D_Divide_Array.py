n = int(input())
array = list(map(int, input().split()))

zero_array = []
positive_array = []
negative_array = []

for num in array:
    if num < 0:
        negative_array.append(num)
    elif num > 0:
        positive_array.append(num)
    else:
        zero_array.append(num)

if len(negative_array) % 2 == 0:
    zero_array.append(negative_array.pop())

if len(negative_array) > 2:
    positive_array.append(negative_array.pop())
    positive_array.append(negative_array.pop())

print(len(negative_array), *negative_array)
print(len(positive_array), *positive_array)
print(len(zero_array), *zero_array)
