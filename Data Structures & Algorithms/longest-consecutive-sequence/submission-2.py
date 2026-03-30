class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums.sort()
        print(nums)
        currCount = 1
        maxLen = 1

        if not nums:
            return 0

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                continue
            
            if nums[i] - nums[i-1] == 1:
                #check that it is increasing
                currCount += 1
            else:
                currCount = 1
                
            maxLen = max(maxLen, currCount)



        

        return maxLen

