class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # naive recursion
        # as soon as the product becomes negative, if the next num isnt negative
        # start fresh
        # update a max value each time we do a reset
        # 1,2,-3,4
        res = nums[0]
        currMax = currMin = 1
        
        for n in nums:
            temp = currMax * n
            currMax = max(n, currMax * n, currMin * n)
            currMin = min(n, temp, currMin * n)
            res = max(res, currMax)
        
        return res
