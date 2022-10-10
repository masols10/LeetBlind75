class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''Time for both dfs and bfs is = number of nodes + number of edges
        Time: O(n + e)
        Space: O(n) + o(n)
        Auxiliary Space: O(n)'''
        if not grid or not grid[0]:
            return 0
        
        islands = 0
        visit = set()
        rows, cols = len(grid), len(grid[0])
        
        def dfs(r, c):
            if (r not in range(rows) or
                c not in range(cols) or
                grid[r][c] == "0" or
                (r, c) in visit):
                return
            
            visit.add((r, c))
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in directions:
                dfs(r + dr, c + dc)
                
        def bfs(r, c):
            q = collections.deque()
            visit.add((r, c))
            q.append((r, c))
            
            while q:
                row, col = q.popleft()
                directions = [[1,0],[-1,0],[0,1],[0,-1]]
                
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r in range(rows) and c in range(cols) and grid[r][c] == "1" and (r, c) not in visit):
                        q.append((r, c))
                        visit.add((r, c))
                    
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    islands += 1
                    #dfs(r, c)
                    bfs(r, c)
        return islands
        