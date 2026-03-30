class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # return length of shortest subarary whose sum is greater or equal to target
        # target = 10, nums = [2,1,5,1,5,3] ans = 5 + 1 + 5 >= 10 --> 3
        # dynamic sliding window problem
        # update a min value each time we find a new window that meets the condition
        # left starts at 0, right starts at left + 1
        # keep track of a currSum and currNums
        # keep increasing right pt until the added sum is >= target
        # do this for the entire array

        curSum = 0
        minLen = float('inf')
        left = 0
        for right in range(len(nums)):
            curSum += nums[right]
            while curSum >= target:  # shrink while valid
                minLen = min(minLen, right - left + 1)
                curSum -= nums[left]  # subtract left element
                left += 1             # shrink window
    
        return minLen if minLen != float('inf') else 0
