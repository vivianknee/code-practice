class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        q = deque()

        def addCell(r, c):
            if (min(r, c) < 0 or r == ROWS or c == COLS or
                (r, c) in visit or grid[r][c] == -1
            ):
                return
            visit.add((r, c))
            q.append([r, c])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r, c])
                    visit.add((r, c))

        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                addCell(r + 1, c)
                addCell(r - 1, c)
                addCell(r, c + 1)
                addCell(r, c - 1)
            dist += 1

        
        # backtracking too slow
        # INF = 2147483647
    
        # def dfs(x, y, visited):
        #     directions = [[0,1],[0,-1],[1,0],[-1,0]]
        #     minPath = INF
        #     # out of bounds
        #     if x < 0 or y < 0 or x >= rows or y >= cols:
        #         return INF
            
        #     # wall or already visited
        #     if grid[x][y] == -1 or (x, y) in visited:
        #         return INF
            
        #     # found treasure!
        #     if grid[x][y] == 0:
        #         return 0
            
        #     visited.add((x, y))

        #     # keep traversing
        #     for d in directions:
        #         x_new = x + d[0]
        #         y_new = y + d[1]
                 
        #         result = dfs(x_new, y_new, visited)
        #         minPath = min(minPath, result + 1)

        #     visited.remove((x, y))

        #     return minPath
        
        

        # for r in range(rows):
        #     for c in range(cols):
        #         if grid[r][c] == INF: # found a starting point
        #             grid[r][c] = dfs(r,c, set())
        

