class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        # length of longest subtring with at most two diff char
        # dynamic window
        # we can have a dict
        # each time we check a new value, we make sure
            # if the dict has a len less than 2
                # either we are seeing a new char
                    # add 1 to freq
                # or a char we havent seen before
                    # add to the dict and set to 1
            # if the set has a len greater than 2, we need to adjust our window size
                # need to shrink the window till it no longer contains the
                # earliest char we saw in our dict
                # we can do this with a left pointer
                # increase left pointer till the char freq is 0, then remove it
        
        seen = {}
        l = 0
        res = float('-inf')
        for r in range(len(s)):
            curChar = s[r]
            # check the len of seen
            if curChar in seen:
                seen[curChar] += 1
            # set to 1
            else:
                seen[curChar] = 1
            
            while len(seen) > 2:
                leftChar = s[l]
                seen[leftChar] -= 1
                if seen[leftChar] == 0:
                    del seen[leftChar]
                l += 1

            res = max(res, r-l + 1)
        
        return res
            
            

        