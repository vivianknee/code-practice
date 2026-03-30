class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # naive approach
        # nested for loop
        # for each num in nums, create a pair for that num alone, and then with each of its neightbors
        # store these pairs in a set to avoid duplicates

        res = []

        subset = []
        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            # decision to include nums[i]
            subset.append(nums[i])
            dfs(i + 1)

            # decision not to include nums[i]
            subset.pop()
            dfs(i + 1)
        
        dfs(0)
        return res