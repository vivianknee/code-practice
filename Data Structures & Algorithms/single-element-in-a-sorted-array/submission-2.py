class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # have an adj list where each num has a initial value of 2
        # each time we encounter a num, we deincremnt its counter
        # when it reaches 0, we remove it from the lsit
        # the remaining number shud be the element that appears only once

        l = 0
        r = len(nums) - 1
        while l <= r:
            m = l + ((r - l) // 2)
            if (m - 1 < 0 or nums[m-1] != nums[m]) and (m + 1 == len(nums) or nums[m] != nums[m+1]):
                return nums[m]

            leftSize = m - 1 if nums[m-1] == nums[m] else m
            if leftSize % 2:
                r = m - 1
            else:
                l = m + 1


        # o(n) time and space
        # adjList = {num : 2 for num in nums}
        # for num in nums:
        #     if num in adjList:
        #         adjList[num] -= 1
        #         if adjList[num] == 0:
        #             del adjList[num]
        
        # key, val = adjList.popitem() 
        # return key
