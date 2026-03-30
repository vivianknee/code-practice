class Solution:
    def mySqrt(self, x: int) -> int:
        # to get the sqrt of x rounded down we can just start from 1 and take
        # perfect square till we get x
        # we will take which ever value is <=

        l = 0
        r = x 
        maxRoot = float('-inf')
        while l <= r:
            m = (r + l) // 2

            if m * m == x:
                return m
            elif m * m > x:
                r = m - 1
            else: # m * m < x
                maxRoot = max(m, maxRoot)
                l = m + 1
        
        return maxRoot

