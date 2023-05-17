class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def inBound(r, c):
            if 0 <= r < len(image) and 0 <= c < len(image[0]):
                return True
        
        directions = [(-1, 0), (+1, 0), (0, -1), (0, +1)]
        
        start_color = image[sr][sc]
        
        if image[sr][sc] == color:
            return image
        
        def dfs(row, column):
            if image[row][column] != color:
                image[row][column] = color
                
            for dr, dc in directions:
                new_row = dr+row
                new_col = dc+column
                
                if inBound(new_row, new_col) and image[new_row][new_col] == start_color:
                    dfs(new_row, new_col)
            
        
        dfs(sr, sc)
        
        return image