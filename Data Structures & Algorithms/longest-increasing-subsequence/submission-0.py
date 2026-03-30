class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # 9 1 4 2 3 3 7
        # subproblem is lis at each index

        # iterate through nums
        # res value set to -inf
        dp = [1] * (len(nums) + 1) # length, max lis at that index length
        
        for i in range(1, len(nums)):
            for j in range(i):  # check all previous
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], 1 + dp[j])

        return max(dp) # lis for most recent in dp is lis for this list of nums

