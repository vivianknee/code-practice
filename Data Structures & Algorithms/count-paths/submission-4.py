class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # memoization
        # bottom row is all ones by logic
        row = [1] * n
        # iterate row by row, not including last row since we already have it
        for i in range(m - 1):
            # initialize new row to 1
            newRow = [1] * n
            # n - 2 starts at the second to last col
            for j in range(n - 2, -1, -1):
                # add value from right
                newRow[j] = newRow[j + 1] + row[j]
            # replace row with new row each time to carry on values from down
            row = newRow
        
        # return origin
        return row[0]

        
        # O(2^(m+n)) SLOWWW
        # recursivley call for as long as there is a path left to follow
        # def dfs(x, y):
        #     if x==0 and y == 0:
        #         return 1
            
        #     # top edge
        #     if x == 0:
        #         return dfs(x, y - 1)

        #     # left edge
        #     if y == 0:
        #         return dfs(x-1, y)

        #     # up or left
        #     return dfs(x-1, y) + dfs(x, y-1)

        # return dfs(m-1,n-1)


        