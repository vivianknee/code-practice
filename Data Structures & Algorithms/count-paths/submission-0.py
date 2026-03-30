class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # can only move down or right at a time
        # m rows x n cols grid
        # return number of unique paths form (0,0) to (m-1, n-1)

        # two options
            # go down increase m
            # go right increase n
            # if we hit an edge, we stop that recursive call, its not a possible path. 
        
        # take pos in the grid
        # recursivley call for as long as there is a path left to follow
        def dfs(x, y):
            if x==0 and y == 0:
                return 1
            
            # top edge
            if x == 0:
                return dfs(x, y - 1)

            # left edge
            if y == 0:
                return dfs(x-1, y)

            # up or left
            return dfs(x-1, y) + dfs(x, y-1)

        return dfs(m-1,n-1)


        