class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        graph = defaultdict(list)
        for u, v, w in times:
            graph[u]. append((v, w))
        
        timeTakes = [inf] * n
        timeTakes[k - 1] = 0
        heap, visited = [(0, k)], set()
        while heap:
            dist, node = heapq.heappop(heap)
            visited.add(node)
            for nb, w in graph[node]:
                if nb not in visited:
                    heapq.heappush(heap, (dist + w, nb))
                    timeTakes[nb - 1] = min(timeTakes[nb - 1], w + dist)
        
        if inf not in timeTakes:
            return max(timeTakes)
        
        return -1
            

        