class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = triangle[-1].copy()
        rows = len(triangle) # len of last row

        for r in range(rows-2, -1, -1): # start from second to last row
            for c in range(len(triangle[r])):
                dp[c] = triangle[r][c] + min(dp[c], dp[c+1])
        return dp[0]
        # triangle only has a root node
        # if len(triangle) == 1:
        #     return triangle[0][0]
        # # nothing in triangle
        # if not triangle:
        #     return 0

        # # memoize this!!!
        # memo = {} # stores index of value, min at that point
        # def dfs(row, col): # takes an index
        #     if row == len(triangle):
        #         return 0

        #     if (row, col) in memo:
        #         return memo[(row, col)]

        #     # num in row
        #     res = triangle[row][col] + min(dfs(row + 1, col), dfs(row + 1, col + 1))
        #     memo[(row, col)] = res
        #     return memo[(row, col)]
        
        # return dfs(0,0)
