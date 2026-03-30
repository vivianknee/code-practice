class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # dynamic subarray
        # we keep track of a flip variable. 0 meainig we haven't flipped a int yet and 1 otherwise
        # keep track of the size of our window as well in a max variable
        # expand our array
            # when we hit our first 0, we can flip it and continue
            # when we hit our second zero, we need to shrink our window 
            # shrink till we reach the first zero we flipped
            # expand till we reach the end of nums
        
        flipped = 0
        res = float('-inf')
        l = 0
        for r in range(len(nums)):
            # encountered another zero, need to restart subarray
            if flipped == 1 and nums[r] == 0:
                flipped = 0 
                while nums[l] != 0: # until we reach the first zero we flipped
                    l += 1 # increment l pointer
                l += 1 # stop one past the zero
    
            if nums[r] == 0:
                flipped = 1
            res = max(res, r - l + 1)

        return res