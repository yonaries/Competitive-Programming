
def helpful_math():
    s = input()
    s = s.replace('+', '')
    s = sorted(s)
    s = '+'.join(s)
    print(s)


helpful_math()
