class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        word = s.lower()

        for ch in word:
            if ch.isalpha() or ch.isdigit():
                continue
            else:
                word = word.replace(ch, "")
        
        left = 0
        right = len(word)-1

        while left < right:
            if word[left] != word[right]:
                return False
            else:
                left += 1
                right -= 1

        return True

        