class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # 1 is land, 0 is water
        # edges are all water
        # area of an island is defined as number of cells within the island
        # return the max area of an island in grid

        # recursive function
            # check neighbors of the current index passed in as parameters
            # if the neighbor is a 1, we add to island area count and call the recursion on that neighbor
            # we do this until we paint that entire island.
            # replace the 1s with 0s to indicate we have already visited that cell
        
        # main function
            # iterate cell over cell in the matrix
            # when we hit a new 1, it means a new island
            # update a new max if it exists

        # how do we keep track of the curr area of each island?
        # when we hit a 1, we want to increase the count by 1
        # we can pass in a parameter to keep track of area, increasing by 1 each time we call the recursion
        def recursion(x, y, board):
            board[x][y] = 0
            area = 1
            directions = [[0,1], [0,-1], [-1,0], [1,0]]

            for d in directions:
                x_new = x + d[0]
                y_new = y + d[1]

                # edge cases
                if x_new < 0 or y_new < 0 or x_new >= len(board) or y_new >= len(board[0]):
                    continue
                
                if board[x_new][y_new] == 1:
                    board[x_new][y_new] = 0
                    area += recursion(x_new, y_new, board)
                    
            return area

        rows = len(grid)
        cols = len(grid[0])
        max_area = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    # recursion returns the area of the island, each time we reach a new island
                    # update the max with the area of the previous island
                    # + 1 to count the current cell as part of the area
                    max_area = max(max_area, recursion(r,c,grid))
        
        return max_area

        