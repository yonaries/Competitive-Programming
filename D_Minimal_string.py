from collections import deque


def minimal_string(sequence):
    t = deque()
    u = deque()

    # append first character of sequence to t

    # last character of t appended to u
    for _ in range(len(t)):
        u.append(t.pop())

    return "".join(u)


sequence = input()
result = minimal_string(sequence)
print(result)
