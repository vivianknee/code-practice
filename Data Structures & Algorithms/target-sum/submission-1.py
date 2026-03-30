class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # naive recursion
        # 2 choices, subtract and add
        # base case is if the sum at that choiuce == target
        # in that case return 1
        def dfs(i, curSum):
            # base case: used all numbers
            if i == len(nums):
                if curSum == target:
                    return 1
                return 0
            
            # two choices: add or subtract nums[i]
            return dfs(i + 1, curSum + nums[i]) + dfs(i + 1, curSum - nums[i])
        
        return dfs(0, 0)