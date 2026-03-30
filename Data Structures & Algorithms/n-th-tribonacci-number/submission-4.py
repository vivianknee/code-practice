class Solution:
    def tribonacci(self, n: int) -> int:
        # bottom up - tabulation
        dp = [0] * (n + 1)
        if n == 0:
            return 0
        if n <= 2:
            return 1
            
        dp[0] = 0
        dp[1] = 1
        dp[2] = 1
        for i in range(3, n + 1):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        
        return dp[-1]
 
        # top down - memoization
        # use a memo to store values we calculate
        # save time by avoiding recalculation
        # memo = {0:0, 1:1, 2:1} # number, value by tribonacci
        # def dfs(x):
        #     if x in memo:
        #         return memo[x]
            
        #     memo[x] = dfs(x-1) + dfs(x-2) + dfs(x-3)
        #     return memo[x]

        # return dfs(n)

        # naive recursion o(3^n)
        # if n == 0:
        #     return 0
        # if n == 1:
        #     return 1
        # if n == 2:
        #     return 2
        
        # return self.tribonacci(n) + self.tribonacci(n + 1) + self.tribonacci(n + 2)