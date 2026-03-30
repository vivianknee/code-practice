class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort array nums to avoid duplicates
        nums.sort()
        # [-1,0,1,2,-1,0,1] [-1,-1,0,0,1,1,2]
        # outer loop is for every i in num
        res = []

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:# i needs to be greater than 0 to check a prev val
                continue

            l, r = i+1, len(nums) - 1
            while l < r:
                currSum = a + nums[l] + nums[r]
                if currSum > 0:
                    r -= 1
                elif currSum < 0:
                    l += 1
                else:
                    res.append([a,nums[l], nums[r]])
                    l+=1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return res
            



