class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        # k is the number of +1 increments i can do
        # figure out after maximizing where i increment using k, gives the greatest freq of a #
        nums.sort()
        l = 0
        windowSum = 0
        res = 0
        
        for r in range(len(nums)):
            windowSum += nums[r]
            
            # Cost = (target * window_size) - window_sum
            # target = nums[r], window_size = r - l + 1
            while nums[r] * (r - l + 1) > windowSum + k:
                windowSum -= nums[l]
                l += 1
            
            res = max(res, r - l + 1)
        
        return res

        
