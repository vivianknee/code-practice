class Solution:
    def numSquares(self, n: int) -> int:
        # top down - memeoization
        memo = {0:0} # base case 0 needs min 0 squares
        
        def dfs(amount):
            minSquares = float('inf')
            if amount in memo:
                return memo[amount] #return min perfect squares for this amount
            
            i = 1
            while i * i <= amount:
                square = i*i
                minSquares = min(minSquares, 1 + dfs(amount - square)) 
                i += 1

            memo[amount] = minSquares
            return memo[amount]
        
        return dfs(n)


        # naive recursion
        # if n == 0:
        #     return 0

        # self.minSquares = float('inf')
        # def dfs(amount):
        #     if amount == 0:
        #         return 1
            
        #     i = 1
        #     while i * i <= amount:
        #         self.minSquares = min(self.minSquares, 1 + dfs(amount - i^2)) 
        #         i += 1
            
        #     return self.minSquares
        
        # return dfs(n)