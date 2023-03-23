def redietElevator(w, et, ef):
    elevator = [ef+et]
    for i in range(4):
        elevator.append(et)

        abs((ef+et)-(i*2))
        # 0 3 6 9 12
        # 4 2 2 2 2
        # 4 2 0 2 4

        # 4 6 8 10 12

    print(elevator)


if __name__ == '__main__':
    no_test = int(input())
    for _ in range(no_test):
        w, et, ef = map(int, input().split())
        redietElevator(w, et, ef)
