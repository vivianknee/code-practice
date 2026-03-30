class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # return # of possible combinations that add up to target
        # O(n^target)
        # top down memo it
        memo = {} # remaining: # of ways to make it
        def dfs(remaining):
            res = 0
            # base cases
            if remaining == 0: #target met
                return 1
            if remaining < 0: # we went past the target
                return 0 # not a valid sum
            if remaining in memo:
                return memo[remaining]
            
            for num in nums:
                res += dfs(remaining - num)
            memo[remaining] = res

            return res

        return dfs(target)
        
        # for each num in nums, we iterate through nums and add
        # if it hasnt reached target, recursivly call
        # otherwise return 0 







