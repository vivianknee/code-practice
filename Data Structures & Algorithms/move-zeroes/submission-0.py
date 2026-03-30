class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # everything in place
        # count the number of zeros in the array
        # two pointers both starting at the beginning. 
        # first pointer only increments after updating a value
        # second pointer iterates over the array looking for nonzero values

        zeros = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zeros += 1
        remains = len(nums) - zeros

        p1 = p2 = 0
        while p2 < len(nums):
            # second pointer finds a value that is not zero
            if nums[p2] != 0:
                nums[p1] = nums[p2] # put that value in p1 instead
                p1 += 1
            p2 += 1
        
        print(nums)
        
        while p1 < len(nums):
            nums[p1] = 0
            p1+=1
        
        print(nums)
            