class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # choose 1 step or 2 steps
        # cost contains cost of jumping from each step of the stair case
        # you can start from i=0 or i=1
        # return the minimum cost to reach top

        # need to keep track of steps to get to top and also min cost to get to the step
        # bottom up tabulation. 

        # base cases first
        # starting from step 0

        # cache of num of steps
        memo = {}
        def dfs(i):
            if i >= len(cost): # reached the top, no more cost to add
                return 0
            
            if i in memo:
                return memo[i]
            
            memo[i] = cost[i] + min(dfs(i + 1), dfs(i + 2))
            return memo[i]

        # return the min of starting from step 1 vs starting from step 0
        return min(dfs(1), dfs(0))