class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # indexes cannot be the same
        # we want combinations not permutations
        # indexes only need to be within the range of the array, no need to be in order
        # [3,2,3,-3,1,0] target = 3
        # [-3,0,1,2,3,3]

        nums.sort()
        res = []
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:# i needs to be greater than 0 to check a prev val
                    continue

            for j in range(i+1, len(nums)):
                b = nums[j]
                if j > i+1 and nums[j] == nums[j-1]:
                    continue

                l, r = j+1, len(nums) - 1
                while l < r:
                    currSum = a + b + nums[l] + nums[r]
                    if currSum > target:
                        r -= 1
                    elif currSum < target:
                        l += 1
                    else:
                        res.append([a,b,nums[l], nums[r]])
                        l+=1
                        while nums[l] == nums[l-1] and l < r:
                            l += 1
        return res
        