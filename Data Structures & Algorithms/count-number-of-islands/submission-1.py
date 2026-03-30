class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # move horizontally and vertically
        # as long as there is a 1, the island continues
        # for each spot in the grid, check its neighbors
        # use recursion for this
        # if not a single neighbor is a 1, we add to island count and continue looking for the next one.
        
        island_count = 0
        def recursion(x,y, board):
            directions = [[0,1], [0,-1], [-1,0], [1,0]]

            for d in directions:
                x_new = x + d[0]
                y_new = y + d[1]
                
                # edge cases
                if x_new < 0 or y_new < 0 or x_new >= len(board) or y_new >= len(board[0]):
                    continue
                
                if board[x_new][y_new] ==  "1":
                    # mark it as a 0 to signify we already visited it
                    board[x_new][y_new] = "0"
                    recursion(x_new, y_new, board)
                
        rows = len(grid)
        cols = len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    # a new 1 means a new island since we replace 1s with 0s for the curr island
                    island_count += 1
                    recursion(r,c, grid)
                
        return island_count

    # time and space complexity
    # time: i iterate through each item in the grid so time is O(m x n). 
    # i reference the board throughout the recussion so 
    # worst case is the entire grid is filled with ones 
    # so there is m x n recursive calls on the stack thus space is also O(m x n)


        