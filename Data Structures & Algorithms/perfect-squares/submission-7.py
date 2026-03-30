class Solution:
    def numSquares(self, n: int) -> int:
        # bottom up tabulation
        INF = float('inf')
        dp = [INF] * (n + 1)
        dp[0] = 0
        # base case is 0 needs 0 squares
        for i in range(1, n+1): # find min for remaining
            k = 1
            while k*k <= i: # i is the value we currently trying to find min squares for
                dp[i] = min(dp[i], 1 + dp[i-k**2])
                k += 1
        
        return dp[-1]

        # top down - memeoization
        # memo = {0:0} # base case 0 needs min 0 squares
        
        # def dfs(amount):
        #     minSquares = float('inf')
        #     if amount in memo:
        #         return memo[amount] #return min perfect squares for this amount
            
        #     i = 1
        #     while i * i <= amount:
        #         square = i*i
        #         minSquares = min(minSquares, 1 + dfs(amount - square)) 
        #         i += 1

        #     memo[amount] = minSquares
        #     return memo[amount]
        
        # return dfs(n)


        # naive recursion
        # if n == 0:
        #     return 0

        # def dfs(amount):
        #     minSquares = float('inf')
        #     if amount == 0:
        #         return 0
            
        #     i = 1
        #     while i * i <= amount:
        #         minSquares = min(minSquares, 1 + dfs(amount - i^2)) 
        #         i += 1
            
        #     return minSquares
        
        # return dfs(n)