class Solution:
    def jump(self, nums: List[int]) -> int:
        # you can jump up to nums[i]
        # return min # of jumps to reach last position

        # check nums[i]
        # for j in range(nums[i]):
        # we want to jump to the index with the larger jumping range.
        # we either jump past the last index or exactly land, in which case we return # of jumps
        # greedy algorithm
        i = 0
        jumps = 0

        if len(nums) <= 1:
            return 0

        while i < len(nums) - 1:
            # Can reach end from here?
            if i + nums[i] >= len(nums) - 1:
                return jumps + 1
            
            # Find position that lets us reach farthest
            max_reach = 0
            best_index = i + 1
            
            for j in range(1, nums[i] + 1):
                next_pos = i + j
                reach = next_pos + nums[next_pos]  # how far can we go from there?
                if reach > max_reach:
                    max_reach = reach
                    best_index = next_pos
            
            i = best_index
            jumps += 1
        
        return jumps
        