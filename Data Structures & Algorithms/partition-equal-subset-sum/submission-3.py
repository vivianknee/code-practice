class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        if sum(nums) %2 == 1:
            return False
        else:
            target = sum(nums) // 2

        memo = {}
        def dfs(i, remaining):
            if remaining == 0:
                return True   # found a valid subset
            if i >= len(nums) or remaining < 0:
                return False  # out of bounds or overshot
            if (i, remaining) in memo:
                return memo[(i, remaining)]

            # Two choices: include nums[i] or skip it
            result = dfs(i + 1, remaining - nums[i]) or dfs(i + 1, remaining)
            memo[(i, remaining)] = result
            return memo[(i, remaining)]

        return dfs(0,target)


