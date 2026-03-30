# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        # binary search approach
        # left pointer = 1
        # right pointer = n
        # from this we will get a midpoint which is ( l + r) // 2
        # we will guess the midpoint
        # if guess returns 0
            # return midpoint
        # if guess returns -1:
            # we set l = mid + 1
        # if guess returns 1
            # we set r = mid - 1
        
        # we keep doing these checks while l <= r

        l = 1
        r = n
        while l <= r:
            m = (l + r) // 2
            if guess(m) == 0:
                return m
            elif guess(m) == -1:
                r = m - 1
            else: # we return 1
                l = m + 1
                
        











        