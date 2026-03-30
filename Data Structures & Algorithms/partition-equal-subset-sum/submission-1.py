class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        if sum(nums) %2 == 1:
            return False
        else:
            target = sum(nums) // 2
    
        def dfs(i, remaining):
            if remaining == 0:
                return True   # found a valid subset
            if i >= len(nums) or remaining < 0:
                return False  # out of bounds or overshot
            
            # Two choices: include nums[i] or skip it
            return dfs(i + 1, remaining - nums[i]) or dfs(i + 1, remaining)

        return dfs(0,target)

        # 1 2 3 4 # 10, looking for 5

        # 0, 5 looking for 4 OR looking for 5 still

