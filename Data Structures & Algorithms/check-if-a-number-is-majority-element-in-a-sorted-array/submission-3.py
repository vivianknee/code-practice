class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        # one way is to go through and count
        counts = {}
        for i in range(len(nums)):
            if nums[i] in counts:
                counts[nums[i]] += 1
            else:
                counts[nums[i]] = 1
        
        if target in counts and counts[target] > len(nums) // 2:
            return True
        else:
            return False