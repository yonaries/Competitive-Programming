from collections import deque


def yared(testcase):
    stack = deque()

    for num in testcase:
        if not stack:
            stack.append(num)
        else:
            if stack[-1] - num <= 1:
                if stack[-1] <= num:
                    stack.pop()
                elif stack[-1] == num:
                    continue
            else:
                stack.append(num)
            print(stack)
    return stack
    return "YES" if len(stack) == 1 else "NO"


if __name__ == "__main__":
    no_of_test_cases = int(input())
    length_of_string = int(input())

    for _ in range(no_of_test_cases):
        testcase = list(map(int, input().split()))
        result = yared(testcase)
        # print(result)
