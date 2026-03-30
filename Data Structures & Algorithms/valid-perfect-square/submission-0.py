class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # we have a target num
        # one way to see if its a perfect squaer
        # test everynumber starting from 1 till we hopefully get the target num
        # slow, we can do a binary search approach instead

        l = 1
        r = num
        while l <= r:
            mid = (l + r) // 2
            if num < mid * mid:
                r = mid - 1
            elif num > mid * mid:
                l = mid + 1
            else:
                return True
        
        return False
        
