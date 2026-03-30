class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        #iterate through the array
        #if its a one add to a counter
        #if its a zero, reset the counter
        #start at that index
        #but have a max counter variable to compare

        maxOnes = 0
        currOnes = 0

        for num in nums:
            if num == 1:
                currOnes += 1
            else:
                currOnes = 0
            maxOnes = max(maxOnes, currOnes)
        
        return maxOnes

        