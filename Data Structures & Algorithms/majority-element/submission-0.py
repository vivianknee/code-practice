class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        appearances = len(nums)/2
        seen = {}

        for i in range(len(nums)):
            seen[nums[i]] = seen.get(nums[i], 0) + 1

        if max(seen.values()) > appearances:
            return max(seen, key=seen.get)