class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # either return the index of the target or return the index of where
        # the target would be inserted

        l = 0
        r = len(nums) - 1
        
        while l <= r:
            m = (r+l) // 2

            if target < nums[m]:
                r = m - 1
            elif target > nums[m]:
                l = m + 1
            else: # target == nums[m]
                return m

        return l
