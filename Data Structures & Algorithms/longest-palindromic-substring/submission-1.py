class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""

        # look for palindroms starting from center
        # evaultae each char in string as a center
        def expand(s, left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # return the palindrome (left+1 and right-1 because we went one too far)
            return s[left + 1 : right]

        for i in range(len(s)):
            # odd length (center is i)
            odd = expand(s, i, i)
            res = max(res, odd, key=len)
            
            # even length (center is between i and i+1)
            even = expand(s, i, i + 1)
            res = max(res, even, key=len)
        
        return res