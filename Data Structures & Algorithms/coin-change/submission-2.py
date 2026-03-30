class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # bottom up - tabulation
        INF = float('inf')
        dp = [INF] * (amount + 1)
        dp[0] = 0 # at amount 0, 0 coins
        
        for i in range(1, amount + 1): # do it for every amount # 1
            for coin in coins: # first coin is 1
                if i - coin >= 0: # 1 - 1 = 0
                    dp[i] = min(dp[i], 1 + dp[i - coin]) # min of current or min of 1 + amount that remains
            
        if dp[-1] != INF:
            return dp[-1]
        else:
            return -1


        # top down - memoization
        # INF = float('inf')
        # memo = {0:0} # amount : min coins

        # def dfs(amount):
        #     minCoins = float('inf')
        #     if amount in memo:
        #         return memo[amount]
            
        #     if amount == 0:
        #         return 0
            
        #     if amount < 0: # this coin amount will never be the min
        #         return INF
            
        #     for i in range(len(coins)):
        #         minCoins = min(minCoins, 1 + dfs(amount - coins[i]))

        #     memo[amount] = minCoins
        #     return memo[amount]
        
        # ans = dfs(amount)
        # if ans != INF:
        #     return ans
        # else:
        #     return -1

        # # naive recursion
        # # pass the amount
        # # for the amount, iterate through the coins to find min coins
        # # do this for each new amount
        # INF = float('inf')

        # def dfs(amount):
        #     minCoins = float('inf')
        #     if amount == 0:
        #         return 0
            
        #     if amount < 0: # this coin amount will never be the min
        #         return INF
            
        #     for i in range(len(coins)):
        #         minCoins = min(minCoins, 1 + dfs(amount - coins[i]))
            
        #     return minCoins
        
        # ans = dfs(amount)
        # if ans != INF:
        #     return ans
        # else:
        #     return -1

            
