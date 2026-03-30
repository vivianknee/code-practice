class Solution:
    def rob(self, nums: List[int]) -> int:
        # each i in nums is the $$ the ith house has
        # cannot rob two in a row

        # 2,9,8,3,100
        # starting at the first house, you need to consider whether
        # to rob the house you are at or the one after
            # you rob every other house essentially
            # two recursive calls.
            # one starts at the first house, one at the second
            # return the max

        # top down. - memoization
        # what to memorize? keep track of the path that gets the max at a specific index
        memo = {} # (index, moneyMax)
        def recursion(index):
            # base case
            if index > len(nums) - 1: # past last house
                return 0
            
            if index in memo:
                return memo[index]

            # rob at curr index
            rob = nums[index] + recursion(index + 2)
            # rob at next house instead
            skip = recursion(index + 1)
            if rob is None:
                memo[index] = skip
            elif skip is None:
                memo[index] = skip
            else:
                memo[index] = max(rob, skip)
            return memo[index]

        return recursion(0)

        # naive recurison
        # def recursion(index):
        #     # base case
        #     if index > len(nums) - 1: # past last house
        #         return 0
                
        #     # rob at curr index
        #     rob = nums[index] + recursion(index + 2)

        #     # rob at next house instead
        #     skip = recursion(index + 1)
        #     return max(rob, skip)

        # return recursion(0)
