class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # return # of possible combinations that add up to target
        # O(n^target)
        # bottom up
        dp = [0] * (target + 1) #index represents sum, value is the ways
        dp[0] = 1 # 0 ways to make 0
        
        for i in range(1, target + 1):
            for num in nums:
                if (i - num) < 0: # not a valid way
                    continue
                dp[i] += dp[i-num]
                
        return dp[target]

        # top down memo it
        # memo = {} # remaining: # of ways to make it
        # def dfs(remaining):
        #     res = 0
        #     # base cases
        #     if remaining == 0: #target met
        #         return 1
        #     if remaining < 0: # we went past the target
        #         return 0 # not a valid sum
        #     if remaining in memo:
        #         return memo[remaining]
            
        #     for num in nums:
        #         res += dfs(remaining - num)
        #     memo[remaining] = res

        #     return res

        # return dfs(target)
        
        # for each num in nums, we iterate through nums and add
        # if it hasnt reached target, recursivly call
        # otherwise return 0 







