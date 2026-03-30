class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [0]*len(nums)
        currPrefix = 1
        currSuffix = 1
        
        #prefix run
        for prefix in range(len(nums)):
            output[prefix] = currPrefix
            currPrefix *= nums[prefix]
        
        #suffix run
        for suffix in range(len(nums)-1,-1,-1):
            output[suffix] *= currSuffix
            currSuffix *= nums[suffix]



        return output

            
