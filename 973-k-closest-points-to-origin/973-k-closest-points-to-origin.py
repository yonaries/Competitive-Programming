class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x,y in points:
            heapq.heappush(heap,((math.sqrt(x**2 + y**2)),[x,y]))
            
        output = []
        i = 1
        while heap and i <= k:
            h= heapq.heappop(heap)
            output.append(h[1])
            i +=1
        return output