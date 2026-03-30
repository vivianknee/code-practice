class Solution:
    def rob(self, nums: List[int]) -> int:
        # each i in nums is the $$ the ith house has
        # cannot rob two in a row
        
        # bottom up - tabulation and for loops
        # base cases
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        # initalizing my table
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        # going through remaining
        for i in range(2, len(nums)):
            # max of up to house before or two house back and current house
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])

        return dp[-1]

        # top down. - memoization
        # what to memorize? keep track of the path that gets the max at a specific index
        # memo = {} # (index, moneyMax)
        # def recursion(index):
        #     # base case
        #     if index > len(nums) - 1: # past last house
        #         return 0
            
        #     if index in memo:
        #         return memo[index]

        #     # rob at curr index
        #     rob = nums[index] + recursion(index + 2)
        #     # rob at next house instead
        #     skip = recursion(index + 1)
        #     if rob is None:
        #         memo[index] = skip
        #     elif skip is None:
        #         memo[index] = skip
        #     else:
        #         memo[index] = max(rob, skip)
        #     return memo[index]

        # return recursion(0)

        # naive recurison
        # def recursion(index):
        #     # base case
        #     if index > len(nums) - 1: # past last house
        #         return 0
                
        #     # rob at curr index
        #     rob = nums[index] + recursion(index + 2)

        #     # rob at next house instead
        #     skip = recursion(index + 1)
        #     return max(rob, skip)

        # return recursion(0)
