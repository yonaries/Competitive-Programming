size = input()

for i in range(int(size)):
    word = input()
    shorten = []
    if len(word) > 10:
        sum = 0
        shorten.append(word[0])
        for j in range(1, len(word)-1):
            sum += 1
        shorten.append(str(sum))
        shorten.append(word[-1])
        shorten = ''.join(shorten)
        print(shorten)
    else:
        print(word)
