class Solution:
    def maxDifference(self, s: str) -> int:
        if not s:
            return 0  # or raise ValueError("Empty string not allowed")

        # Count character frequencies
        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1

        maxOdd = float('-inf')
        minEven = float('inf')

        for count in freq.values():
            if count % 2 == 0:
                minEven = min(minEven, count)
            else:
                maxOdd = max(maxOdd, count)

        # Handle case: no odd or no even values
        if maxOdd == float('-inf') or minEven == float('inf'):
            return 0  # or handle as needed (e.g., return maxOdd or minEven directly)

        return maxOdd - minEven
