class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # can only hold one stock at a time --> cannot buy two days in a row
        # prices = [7,1,5,3,6,4] ans = 7
        # if we buy on day 1, cant buy day 2, so buy day 2:
            # buy day 1 (p = 1) sell day 2 (p = 5)
            # buy today or buy next day? 
            # buy day 4 ( p= 3)
            # sell day 5 ( p = 6)
            #5-1 = 4 6 -3 =3 4 + 3 = 7
        
        # dfs recursive approach 
        # keep track if of a max profit
        # two choices: buy today or buy tmrw
        # base case is that we reach the end of prices, no days left to buy or sell
        # we want to pass a value to indicate whether the prev transaction we bought or sold
        # we can memoize this to turn it into a top down dp solution
        # naive recursion
        memo = {} # this dict holds (index, canbuy) and the max profit at this point
        def dfs(index, canBuy):
            # base case
            if index == len(prices):
                return 0 # no profit to be made
            
            if (index, canBuy) in memo:
                return memo[(index, canBuy)]

            # choices
            if canBuy:
                # buy tmrw vs buy today
                memo[(index, canBuy)] = max(dfs(index + 1, True), -prices[index] + dfs(index + 1, False))
            else: # cannot buy meaning we must sell
                # sell today, or sell tmrw
                memo[(index, canBuy)] = max(prices[index] + dfs(index + 1, True), dfs(index + 1, False)) 
            return memo[(index, canBuy)]

        return dfs(0, True)
            





