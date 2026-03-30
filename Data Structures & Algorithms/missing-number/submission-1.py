class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # the n ints in nums can be any num from 0-n inclusive
        # O(1) space and O(n) solution

        # get the sum of it shud be
        arr_sum = 0
        for i in range(len(nums) + 1):
            arr_sum += i
        
        res = arr_sum
        for i in range(len(nums)):
            res = res - nums[i]
        
        return res
        


        # brute force O(n) time and space
        # do this n times to find which num is missing in the range
        # create a hashset pre loaded w nums from 0 to n. pop from set when we find the num

        # hashset = set()
        # for i in range(len(nums) + 1):
        #     hashset.add(i)
        
        # for i in range(len(nums)):
        #     if nums[i] in hashset:
        #         hashset.remove(nums[i])
        
        # val = hashset.pop()
        # return val