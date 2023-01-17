def compare(string1, string2):
    string1 = string1.lower()
    string2 = string2.lower()
    for x, y in zip(string1, string2):
        if ord(x) < ord(y):
            return - 1
        elif ord(x) > ord(y):
            return 1
    return 0


s1 = input()
s2 = input()

print(compare(s1, s2))
