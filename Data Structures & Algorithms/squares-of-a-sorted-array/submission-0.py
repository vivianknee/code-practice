class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # nums is in increasing order
        # return an array of the square of each number in increasing order as well

        # iterate over nums
        # perform square operation on each number
        # replace the number with the squared number
        # negative numbers squared may be larger than posiitive
        # list may require sorting

        for i, n in enumerate(nums):
            squared = n**2
            nums[i] = squared
        nums.sort()
        return nums
        