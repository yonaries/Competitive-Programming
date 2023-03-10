class MyCircularDeque:

    def __init__(self, k: int):
        self.limit = k
        self.size = 0
        self.queue = deque()

    def insertFront(self, value: int) -> bool:
        if self.size == self.limit:
            return False
        
        self.queue.appendleft(value)
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.size == self.limit:
            return False
        
        self.queue.append(value)
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.size:
            self.queue.popleft()
            self.size -= 1
            return True
        
        return False

    def deleteLast(self) -> bool:
        if self.size:
            self.queue.pop()
            self.size -= 1
            return True
        
        return False

    def getFront(self) -> int:
        if self.size:
            x = self.queue.popleft()
            self.queue.appendleft(x)
            return x
        
        return -1

    def getRear(self) -> int:
        if self.size:
            x = self.queue.pop()
            self.queue.append(x)
            return x
        
        return -1

    def isEmpty(self) -> bool:
        if len(self.queue) == 0:
            return True
        
        return False

    def isFull(self) -> bool:
        if len(self.queue) == self.limit:
            return True
        
        return False


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()