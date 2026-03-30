class Solution:
    def validPalindrome(self, s: str) -> bool:
        # two pointer
        # one at beginning, one at end
        # we increment and deincrement pointers if the left and right char are equal
        # when two char are not equal, we have the choice to del at most ONE char
        # compare l with r - 1 and compare r with l + 1,
        # if either of these are matches, we can say that char was "deleted" and double
        # increment on which ever side we deleted the char on

        def isPalindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
    
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                # Try skipping left OR skipping right
                return isPalindrome(l + 1, r) or isPalindrome(l, r - 1)
        
        return True

        # s="acdccba" 


        