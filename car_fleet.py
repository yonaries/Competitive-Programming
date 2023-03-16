from collections import deque


def carFleet(target: int, position: list[int], speed: list[int]) -> int:
    stack = deque()

    speed_time = [(x, y) for x, y in zip(position, speed)]
    speed_time.sort()

    for (pos, velocity) in speed_time:
        time = (target-pos)/velocity

        while stack and stack[-1] <= time:
            stack.pop

        stack.append(time)

    print(stack)
    return len(stack)


target = 12
position = [10, 8, 0, 5, 3]
speed = [2, 4, 1, 1, 3]

result = carFleet(target, position, speed)
print(result)
