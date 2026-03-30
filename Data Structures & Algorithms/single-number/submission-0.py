class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # O(1) space means i cant use a set
        res = 0
        for n in nums:
            res = n ^ res
        return res