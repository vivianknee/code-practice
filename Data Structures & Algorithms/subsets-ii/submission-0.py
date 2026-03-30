class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        nums.sort()

        def backtrack(i):
            if i == len(nums):
                # reached a leaf node
                res.append(subset.copy())
                return
            
            subset.append(nums[i])
            # use the curr element
            backtrack(i + 1)
            subset.pop()
            # dont use the curr element

            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1)
        
        backtrack(0)
        return res