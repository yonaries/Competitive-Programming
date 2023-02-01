if __name__ == '__main__':
    size = int(input())
    sum = 0

    for i in range(size):
        coordinate = input().split()
        for num in coordinate:
            sum += int(num)

    print("YES" if sum == 0 else "NO")
