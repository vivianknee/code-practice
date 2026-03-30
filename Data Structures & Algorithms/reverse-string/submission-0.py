class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # s = ["n","e","e","t"]
        # l starting at n
        # r starting at t
        # s = ["t","e","e","n"] l = 0 --> 1 r = len(s) - 1 --> -1
        l = 0
        r = len(s) - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        
        return s
        