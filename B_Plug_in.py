from collections import deque


def remove_duplicate_letters(s):
    stack = deque()

    for c in s:
        if stack and c == stack[-1]:
            stack.pop()
        else:
            stack.append(c)

    return ''.join(stack)


string = input()
result = remove_duplicate_letters(string)
print(result)
