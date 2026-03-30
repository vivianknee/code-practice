class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # if surrounded by Xs, replaces Os with Xs in place
        # impossible for a zero touching the border to be surrounded
        # start dfs from zeros touching the border. 
        # if a zero is touching the border zero, it too cannot be surrouned
        # store these cells in a set.
        # then go through the board and set all cells not in the set to X

        safe = set()
        rows, cols = len(board), len(board[0])

        def dfs(x, y):
            # determines what to add to safe
            # dont count a cell as safe if
                # out of bounds
                # its an X
                # its already in safe
            if (x,y) in safe or x < 0 or y < 0 or x >= rows or y >= cols or board[x][y] == "X":
                return

            safe.add((x,y))
            dfs(x+1,y)
            dfs(x-1,y)
            dfs(x,y+1)
            dfs(x,y-1)

        # call dfs for every possible O
        for c in range(cols):
            dfs(0, c) # top
            dfs(rows-1, c) # bottom

        for r in range(rows):
            dfs(r, 0) # left
            dfs(r, cols-1) # right

        for r in range(rows):
            for c in range(cols):
                if (r,c) not in safe:
                    board[r][c] = "X"
        


                    



        