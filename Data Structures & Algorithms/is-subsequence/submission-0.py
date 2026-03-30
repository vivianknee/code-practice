class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sub = whole = 0

        while whole < len(t):
            if sub < len(s) and t[whole] == s[sub]:
                sub += 1
            whole += 1
            
        return len(s) == sub