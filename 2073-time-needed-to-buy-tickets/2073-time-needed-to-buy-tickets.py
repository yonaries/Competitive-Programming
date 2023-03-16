class Solution:
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        queue = deque()

        for index, no in enumerate(tickets):
            queue.append((index, no))

        time = 0
        while queue:
            if len(queue) == 1:
                time += queue[0][1]
                break

            if queue[0][1] == 1:
                if k == queue[0][0]:
                    time += 1
                    break
                else:
                    queue.popleft()

            else:
                (p, t) = queue.popleft()
                queue.append((p, t-1))

            time += 1

        return time
