class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        ROWS = len(isConnected)
        visited = set()
        provinces = 0
    
        def dfs(city):
            visited.add(city)
            
            for neighbor in range(ROWS):
                if isConnected[city][neighbor] == 1 and neighbor not in visited:
                    dfs(neighbor)
    
        for city in range(ROWS):
            if city not in visited:
                dfs(city)
                provinces += 1
    
        return provinces
                