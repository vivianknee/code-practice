class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #two pointer, one left one right
        #if sum of the two is greater than target, move the smaller of the indices

        seen = {}
        for i, n in enumerate(nums):
            complement = target - n
            if complement in seen:
                return [seen[complement], i]
            #updaing the hashmap
            seen[n] = i

        