class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # have an adj list where each num has a initial value of 2
        # each time we encounter a num, we deincremnt its counter
        # when it reaches 0, we remove it from the lsit
        # the remaining number shud be the element that appears only once

        adjList = {num : 2 for num in nums}
        for num in nums:
            if num in adjList:
                adjList[num] -= 1
                if adjList[num] == 0:
                    del adjList[num]
        
        key, val = adjList.popitem() 
        return key
