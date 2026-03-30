class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # greedy solution
        # start at the end. set the goal post which is the index at the end
        # compare to the value before, is it possible for the i + nums[i] can get to the goal post?
        # if yes, update the goal post, continue

        goal = len(nums) - 1 # last num
        for i in range(len(nums) - 2, -1, -1): # start at second to last value for analysis
            if i + nums[i] >= goal:
                goal = i
        
        if goal == 0:
            return True
        else:
            return False

        # miracle brute force o(n^2) solution lol!
        # i = 0
        # index_total = len(nums) - 1

        # if len(nums) == 1:
        #     return True
        
        # while i < index_total: # if we in this while loop it means we are not at the end
        #     # every possible jump length we cud do
        #     best_reach = 0
        #     best_jump = 0
        #     for j in range(nums[i], 0, -1):
        #         if i + j >= index_total:
        #             return True
        #         elif nums[i + j] != 0: # we dont want to land on a zero
        #             reach = j + nums[i + j]
        #             if reach > best_reach:
        #                 best_reach = reach
        #                 best_jump = j
            
        #     if best_jump == 0:  # stuck, no valid jumps
        #         return False
            
        #     i += best_jump

        # return False
        