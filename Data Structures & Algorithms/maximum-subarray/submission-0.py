class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # given array nums, find the subarray with the largest sum
        # return that largest sum

        maxSub = nums[0]
        curSum = 0
        for n in nums:
            if curSum < 0:
                curSum = 0
            curSum += n
            maxSub = max(maxSub, curSum)
        
        return maxSub
