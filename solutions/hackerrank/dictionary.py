size = list(map(int, input().split(' ')))
groupA = []
groupB = []
dic = {}

# accepting group a characters
for i in range(size[0]):
    groupA.append(input())

# accepting group b characters
for i in range(size[1]):
    groupB.append(input())


# tracking indices of characters in groupA
for i, ch in enumerate(groupA):
    if ch in dic:
        dic[ch] += [str(i+1)]
    else:
        dic[ch] = [str(i+1)]

# checking if character from groupB has happens in groupA
for ch in groupB:
    if ch in dic:
        print(' '.join(dic.get(ch)))
    else:
        print(-1)
