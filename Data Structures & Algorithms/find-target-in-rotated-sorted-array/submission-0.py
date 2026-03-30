class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l+r) // 2
            if target == nums[mid]:
                return mid
            
            #left sorted portion
            if nums[mid] >= nums[l]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else: #target < mid but greater than left
                    r = mid - 1
            #right sorted portion
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else: #greater than mid and less than right
                    l = mid + 1
        return -1
                


