class Solution:
    def countSubstrings(self, s: str) -> int:
        
        res = 0
        def expand(s, l, r):
            count = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
            return count
        
        for i in range(len(s)):
            odd = expand(s, i, i)
            even = expand(s, i, i+1)
            res += odd + even
            
        return res

        