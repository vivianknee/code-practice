class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # get the new index by adding the value at the prev index to the index
        # so we never want to land on a zero if we can help it.
        # so given our jump, we want to determine the farthest place we can land that is not a zero

        # how do we determine the farthest we can go that is not a zero?
            # we can start with the largest jump
        

        i = 0
        index_total = len(nums) - 1

        if len(nums) == 1:
            return True
        
        while i < index_total: # if we in this while loop it means we are not at the end
            # every possible jump length we cud do
            best_reach = 0
            best_jump = 0
            for j in range(nums[i], 0, -1):
                if i + j >= index_total:
                    return True
                elif nums[i + j] != 0: # we dont want to land on a zero
                    reach = j + nums[i + j]
                    if reach > best_reach:
                        best_reach = reach
                        best_jump = j
            
            if best_jump == 0:  # stuck, no valid jumps
                return False
            
            i += best_jump

        return False
        