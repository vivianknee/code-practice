class Solution:
    def tribonacci(self, n: int) -> int:
        # top down - memoization
        # use a memo to store values we calculate
        # save time by avoiding recalculation
        memo = {0:0, 1:1, 2:1} # number, value by tribonacci
        def dfs(x):
            if x in memo:
                return memo[x]
            
            memo[x] = dfs(x-1) + dfs(x-2) + dfs(x-3)
            return memo[x]

        return dfs(n)

        # naive recursion o(3^n)
        # if n == 0:
        #     return 0
        # if n == 1:
        #     return 1
        # if n == 2:
        #     return 2
        
        # return self.tribonacci(n) + self.tribonacci(n + 1) + self.tribonacci(n + 2)