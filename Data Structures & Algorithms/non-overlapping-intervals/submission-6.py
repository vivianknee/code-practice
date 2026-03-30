class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # return the min number of intervals you. need to remove to make remaining
        # intervals non overlapping
        intervals.sort()
        res = 0
        prevEnd = intervals[0][1]

        for start,end in intervals[1:]:
            if start >= prevEnd: # no overlap
                prevEnd = end # update prev end to the larger since if they dont over lap
                # nexxt end is surely larger
            else: # overlap means we increase removal count
                res += 1
                prevEnd = min(end, prevEnd) #curr end cud end within prev interval or after. 
                # we remove the one that ends farther and keep the one ending sooner thus 
                # save the minimum
        return res
        # if no intervals, min to remove is 0
        # if not intervals:
        #     return 0

        # # to make my life easier, i want to sort the intervals by the first num
        # # [1,2] [2,4] [1,4] --> [1,2] [1,4] [2,4]
        # intervals.sort(key=lambda x: x[1])  
        # og = len(intervals)

        # # to determine whether or not intervals are overlapping, we compare the inner two nums
        # i = 0
        # while i < len(intervals):
        #     if i+1 < len(intervals) and intervals[i][1] > intervals[i + 1][0]:
        #         # we can remove the second interval 
        #         # (either or, shudnt matter too much since we sorted intervals)
        #         del intervals[i+1]
        #     else:
        #         # increment if the two curr intervals have no overlap. this way we dont skip over
        #         i += 1
        
        # # the difference in lengths shud be the min intervals removed
        # return og - len(intervals)
