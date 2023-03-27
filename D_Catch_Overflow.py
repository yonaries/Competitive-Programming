from collections import deque


class Memory:
    def __init__(self):
        self.x = 0
        self.loop = 0
        self.stack = deque()
        self.overflow = False

    def add(self):
        if not self.overflow:
            if self.loop > 0 and self.loop < 2**32 - self.loop - 1:
                self.x += self.loop

            elif not self.loop:
                self.x += 1

            else:
                self.overflow = True

    def end(self):
        if self.stack:
            self.loop //= self.stack.pop()
        else:
            self.loop = 0

    def for_(self, n):
        if not self.overflow:
            if not self.stack:
                self.stack.append(n)
                self.loop = n

            else:
                self.stack.append(n)
                self.loop *= n


l = int(input())

memory = Memory()

for _ in range(l):
    command = input().split()
    if memory.overflow:
        break

    if command[0] == 'add':
        memory.add()

    elif command[0] == 'for':
        memory.for_(int(command[1]))

    elif command[0] == 'end':
        memory.end()

if memory.overflow:
    print('OVERFLOW!!!')
else:
    print(memory.x)
