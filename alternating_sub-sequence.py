def runCase():
    n = int(input())
    array = list(map(int, input().split()))

    maxneg = float('-inf')
    maxpos = float('-inf')
    maxSum = 0
    turn = -1 if array[0] < 0 else 1
    i = 0

    while i < n:
        if turn == -1:
            while i < n and array[i] < 0:
                maxneg = max(maxneg, array[i])
                i += 1
            maxSum += maxneg
            maxneg = float('-inf')
            turn = 1
        else:
            while i < n and array[i] > 0:
                maxpos = max(maxpos, array[i])
                i += 1
            maxSum += maxpos
            maxpos = float('-inf')
            turn = -1
        
    print(maxSum)

if __name__ == '__main__':
    tests = int(input())

    for _ in range(tests):
        runCase()
