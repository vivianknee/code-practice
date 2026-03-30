class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # top down - memoization
        # create memo
        memo = {} #(index in nums, currsum) --> num of ways
        # sub problem is that from that new sum, we see if we can make the sum from the 
        # remaining things in nums
        def dfs(i, curSum):
            if (i, curSum) in memo:
                return memo[(i, curSum)]
            
            # base case: used all numbers
            if i == len(nums):
                if curSum == target:
                    return 1
                return 0
            
            memo[(i, curSum)] = dfs(i + 1, curSum + nums[i]) + dfs(i + 1, curSum - nums[i])
            return memo[i, curSum]
        
        return dfs(0,0)

        # naive recursion
        # def dfs(i, curSum):
        #     # base case: used all numbers
        #     if i == len(nums):
        #         if curSum == target:
        #             return 1
        #         return 0
            
        #     # two choices: add or subtract nums[i]
        #     return dfs(i + 1, curSum + nums[i]) + dfs(i + 1, curSum - nums[i])
        
        # return dfs(0, 0)