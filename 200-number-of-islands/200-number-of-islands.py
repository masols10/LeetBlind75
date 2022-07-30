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
        
'''********************************************************************************************************************************************************************************************

    def numIslands(self, grid: List[List[str]]) -> int:
        # len(grid) provides number of rows in the list grid
        m = len(grid)
        # len(grid[0]) provides the length of each row present in list grid
        n = len(grid[0])
        
        # Depth-first-search algorithm
        def dfs(grid, i, j): # We take three arguments as input, the grid, the co-ordinates of grid, i for rows and j for each element in a row
            if i<0 or j<0 or i>=m or j>=n or grid[i][j]!='1':
                # Check if we are within the grid and if the value at the current position is not 1. If this is the case, then do nothing
                return # This statement is a bare return. This is equivalent to 'return None' statement
            else: # If we are within the grid, we will check if the surrounding grid has value.
                grid[i][j] = '#'
                dfs(grid, i+1, j)
                dfs(grid, i-1, j)
                dfs(grid, i, j+1)
                dfs(grid, i, j-1)
        
        # We initialize a counter for getting the total number of islands in the grid
        num_of_islands = 0
        # For each row in grid
        for i in range(m):
            # For each element of each row
            for j in range(n):
                # We check if the value at which the pointer is pointing is 1
                if grid[i][j] == '1':
                    # If so, we run the dfs algorithm to check if we have any adjacent grid ppositions with value 1
                    dfs(grid, i, j)
                    # We increment the value of island, until we get water in the middle. That is 0.
                    num_of_islands+=1
        return num_of_islands # In the end we return the count of islands

#Approach 2 Go througth all the elements in the matrix and if its LAND i.e '1' , start DFS in all 4 directions until you see WATER i.e '0' or BOUNDARY, each time you see a land cell mark it as visited by changing its value to an arbitary character like '#'.
#Using STACK for DFS will improve on time as it is faster than inbuilt recursive function stack because it has less overhead.

    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        ans = 0
        
        for a in range(m):
            for b in range(n):
                if grid[a][b] == '1':
                    ans += 1
                    stack = [[a,b]]
                    while stack:
                        i, j = stack.pop()
                        grid[i][j] = '#'
                        if i > 0 and grid[i-1][j] == '1':
                            stack.append([i-1,j])
                        if j > 0 and grid[i][j-1] == '1':
                            stack.append([i,j-1])
                        if i < m-1 and grid[i+1][j] == '1':
                            stack.append([i+1,j])
                        if j < n-1 and grid[i][j+1] == '1':
                            stack.append([i,j+1])
        
        return ans '''