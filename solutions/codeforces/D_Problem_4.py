def validHello(word):
    hello = ['o', 'l', 'l', 'e', 'h']
    for letter in word:
        if hello[-1] == letter:
            hello.pop()
            if len(hello) == 0:
                return 'YES'
    return 'NO'


word = input()
print(validHello(word,))
