bracket_seq = input()  # read input string
stack = []  # create an empty stack

for bracket in bracket_seq:
    if bracket == '(':
        stack.append(bracket)
    elif len(stack) > 0 and stack[-1] == '(':
        stack.pop()
    else:
        stack.append(bracket)

print(len(bracket_seq) - len(stack))
