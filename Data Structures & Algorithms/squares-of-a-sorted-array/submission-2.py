class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # nums is in increasing order
        # return an array of the square of each number in increasing order as well

        # iterate over nums
        # perform square operation on each number
        # replace the number with the squared number
        # negative numbers squared may be larger than posiitive
        # list may require sorting

        l = 0
        r = len(nums) - 1
        res = []

        while l <= r:
            if nums[l]*nums[l] > nums[r]*nums[r]:
                res.append(nums[l]*nums[l])
                l+=1
            else:
                res.append(nums[r]*nums[r])
                r-=1
        
        return res[::-1]


        