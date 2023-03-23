def lealem(s):
    s = s.split("+")
    s.sort()
    return "+".join(s)


if __name__ == "__main__":
    string = input()
    result = lealem(string)
    print(result)
