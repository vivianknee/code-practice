class Solution:
    def validPalindrome(self, s: str) -> bool:
        # two pointer
        # one at beginning, one at end
        # we increment and deincrement pointers if the left and right char are equal
        # when two char are not equal, we have the choice to del at most ONE char
        # compare l with r - 1 and compare r with l + 1,
        # if either of these are matches, we can say that char was "deleted" and double
        # increment on which ever side we deleted the char on

        l, r = 0, len(s) - 1

        while l < r:
            if s[l] != s[r]:
                skipL = s[l + 1 : r + 1]
                skipR = s[l : r]
                return skipL == skipL[::-1] or skipR == skipR[::-1]
            l, r = l + 1, r - 1

        return True

        # s="acdccba" 


        