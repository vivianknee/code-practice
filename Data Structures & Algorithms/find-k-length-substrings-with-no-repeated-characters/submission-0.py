class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        if k > len(s):
            return 0
    
        seen = {}
        count = 0
        
        # Build initial window
        for i in range(k):
            seen[s[i]] = seen.get(s[i], 0) + 1
        
        if len(seen) == k:  # all unique
            count += 1
        
        # Slide window
        for r in range(k, len(s)):
            l = r - k
            
            # Add right char
            seen[s[r]] = seen.get(s[r], 0) + 1
            
            # Remove left char
            seen[s[l]] -= 1
            if seen[s[l]] == 0:
                del seen[s[l]]
            
            # Check if valid
            if len(seen) == k:
                count += 1
        
        return count
            