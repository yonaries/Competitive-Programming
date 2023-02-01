testcase = int(input())


def getNextDest(row, col, length):
    return [col, length-1-row]


for _ in range(testcase):
    length = int(input())
    matrix = []
    count = 0
    indices = set()

    for _ in range(length):
        matrix += list(map(int, input().split()))

    for row in range(len(matrix)):
        for col in range(row, len(matrix)-row):
            val = matrix[row][col]
            nextRow, nextCol = getNextDest(row, col, length)
