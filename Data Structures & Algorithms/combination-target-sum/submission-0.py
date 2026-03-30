class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        subset = []
        def backtrack(i):
            # base case
            if sum(subset) == target:
                res.append(subset.copy())
                return

            # another base case
            if sum(subset) > target:
                return

            for j in range(i, len(nums)):
                # make choice to append num to subset
                # recursivly call
                # backtracking step
                subset.append(nums[j])
                backtrack(j)
                subset.pop()
                

        backtrack(0)
        return res