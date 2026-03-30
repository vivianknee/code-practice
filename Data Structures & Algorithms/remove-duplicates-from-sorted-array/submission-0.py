class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # nums is sorted in increasing order
        # another pointer problem
        # since nums is in sorted order, we only need to compare to the prev
        # since we are del from nums, we can index from the end of the array

        for i in range(len(nums)-1, -1, -1):
            if i < len(nums) - 1 and nums[i] == nums[i + 1]:
                del nums[i+1]
                print(nums)
        
        return len(nums)