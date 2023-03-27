def fixWord(word):
    lowercase = 0
    uppercase = 0

    for letter in word:
        if letter.islower():
            lowercase += 1
        elif letter.isupper():
            uppercase += 1
    if lowercase >= uppercase:
        return word.lower()
    else:
        return word.upper()


word = input()
print(fixWord(word))
