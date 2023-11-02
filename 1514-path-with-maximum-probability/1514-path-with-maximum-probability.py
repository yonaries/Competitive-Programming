class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:

        if start_node == end_node:
            return 0

        graph = defaultdict(list)
        probs, visited = defaultdict(lambda: float('-inf')), set()
        for i in range(len(edges)):
            u, v = edges[i]
            graph[u].append((v, succProb[i]))
            graph[v].append((u, succProb[i]))
        
        heap = [(-1, start_node)]
        while heap:
            prob, node = heapq.heappop(heap)
            probs[node] = max(probs[node], abs(prob))
            visited.add(node)
            for nb, p in graph[node]:
                if nb not in visited:
                    heapq.heappush(heap, (-1 * abs(prob) * p, nb))
        
        res = abs(probs[end_node])
        if res == inf:
            return float(0)
        return res

        