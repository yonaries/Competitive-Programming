class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        # Create an adjacency list to represent the graph
        adj_list = [[] for _ in range(n)]
        
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
    
        # Create a visited array to keep track of visited vertices
        visited = set()
    
        # Create a queue for BFS traversal
        queue = deque([source])
    
        # Mark the source vertex as visited
        visited.add(source)
    
        # Perform BFS traversal
        while queue:
            # Dequeue a vertex from the queue
            node = queue.popleft()
        
            # If we have reached the destination, return True
            if node == destination:
                return True
        
            # Explore all neighbors of the current node
            for neighbor in adj_list[node]:
                if neighbor not in visited:
                    
                    # Mark the neighbor as visited and enqueue it
                    visited.add(neighbor)
                    queue.append(neighbor)
    
        # If we have explored all possible paths and haven't found the destination, return False
        return False
