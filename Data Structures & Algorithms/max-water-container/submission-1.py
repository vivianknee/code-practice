class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        maxArea = 0

        while left < right:
            currArea = (right-left) * min(heights[left], heights[right])
            if heights[left] < heights[right]:
                left += 1
            # elif heights[right] < heights[left]:
            #     right -= 1
            else:
                right -= 1
            
            maxArea = max(currArea, maxArea)
        
        return maxArea


        