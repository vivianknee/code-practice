class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # if the cell is empty, we wanna skip past it
        # iterate over grid for rotten fruits
        # from each rotten fruit, we shud determine the min time for that rotten fruit
        # if a fresh fruit is isolated, the state is impossible
        queue = deque()
        fresh = 0
        rows = len(grid)
        cols = len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                   queue.append((r,c))
                elif grid[r][c] == 1:
                    fresh += 1
        
        # no fresh fruit = 0 min
        if fresh == 0:
            return 0
        
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        minutes = 0
        while queue:
            minutes += 1
            for i in range(len(queue)):  # process entire level
                # gets coordinates of rotten orange
                x, y = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                        grid[nx][ny] = 2  # mark rotten
                        fresh -= 1
                        queue.append((nx, ny))

        return minutes - 1 if fresh == 0 else -1

            
