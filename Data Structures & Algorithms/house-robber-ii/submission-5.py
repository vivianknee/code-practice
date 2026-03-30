class Solution:
    def rob(self, nums: List[int]) -> int:
        # depending where we start in the circle, we can get different results.
        # going through nums, we want to get the max at each index in the list
        # get the max of those maxes
        
        # bottom up - tabulation

        def helper(nums):
            if not nums:
                return 0
            if len(nums) == 1:
                return nums[0]

            dp = [0] * len(nums)
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])

            for i in range(2, len(nums)):
                dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])

            return dp[-1]
        
        if len(nums) == 1:
            return nums[0]
        return max(helper(nums[1:]), helper(nums[:-1]))

        # top down - memoization
        # if len(nums) == 1:
        #     return nums[0]

        # memo = {} # contains index, max money at that point
        # def dfs(lo, hi):
        #     if lo > hi: # gone past the start
        #         return 0
            
        #     if (lo, hi) in memo:
        #         return memo[(lo, hi)]

        #     rob = nums[lo] + dfs(lo + 2, hi)
        #     skip = dfs(lo + 1, hi)
            
        #     memo[(lo, hi)] = max(rob, skip)
        #     return memo[(lo, hi)]
        
        # # Case 1: rob first house, can't rob last
        # case1 = dfs(0, len(nums) - 2)
        # # Case 2: skip first house, can rob last
        # case2 = dfs(1, len(nums) - 1)
        
        # return max(case1, case2)


        # naive recursion
        # if len(nums) == 1:
        #     return nums[0]
    
        # def dfs(lo, hi):
        #     if lo > hi: # gone past the start
        #         return 0
            
        #     rob = nums[lo] + dfs(lo + 2, hi)
        #     skip = dfs(lo + 1, hi)
            
        #     return max(rob, skip)
        
        # # Case 1: rob first house, can't rob last
        # case1 = dfs(0, len(nums) - 2)
        # # Case 2: skip first house, can rob last
        # case2 = dfs(1, len(nums) - 1)
        
        # return max(case1, case2)