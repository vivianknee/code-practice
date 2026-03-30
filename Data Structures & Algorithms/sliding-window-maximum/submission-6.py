class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        res = []

        #initialize the max of the first window
        maxNum = max(nums[:k])
        res.append(maxNum)

        l = 0
        for r in range(k, len(nums)):
            l+= 1
            if nums[l-1] == maxNum: #checks if max is leaving the window, update max accordingly
                maxNum = max(nums[l:r+1])
            elif nums[r] > nums[l]:
                maxNum = max(maxNum, nums[r])
            
            res.append(maxNum)
        
        return res

       
            

            
        

        
        