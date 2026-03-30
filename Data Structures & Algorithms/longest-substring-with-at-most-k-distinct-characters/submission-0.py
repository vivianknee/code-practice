class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        # same as the previous problem
        # dynamic subarray depending on k distinct char
        # dictionary pairing character to freq
        # iterate over s and update freq of char
        # when the len of dict is > k, we want to shrink the window

        seen = {}
        res = 0
        l = 0
        for r in range(len(s)):
            char = s[r]
            if char in seen:
                seen[char] += 1
            else:
                seen[char] = 1
            
            while len(seen) > k:
                leftChar = s[l]
                seen[leftChar] -= 1
                if seen[leftChar] == 0:
                    del seen[leftChar]
                l += 1
            res = max(res, r-l+1)
        return res

        