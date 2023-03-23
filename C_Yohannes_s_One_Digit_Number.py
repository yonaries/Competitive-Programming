import sys
import threading


def input(): return sys.stdin.readline().strip()


def main():
    def yohannes(testcase, count=0):
        if len(testcase) == 1:
            return (count, testcase[0])

        result = list(map(int, str(sum(testcase))))
        return yohannes(list(result), count+1)

    testcase = list(map(int, input().strip()))
    result = yohannes(testcase)[0]
    print(result)


if __name__ == '__main__':

    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
