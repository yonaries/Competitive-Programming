def non_palindrome(string):
    return ''.join(sorted(list(string)))


size = int(input())

for _ in range(size):
    testcase = input()
    if len(set(testcase)) == 1:
        print(-1)
    else:
        print(non_palindrome(testcase))
