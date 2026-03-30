class Solution:
    def merge(self, interval1, interval2):
        # first interval always smaller, since array is sorted 
        # we already know we want to insert here
        return [interval1[0], max(interval1[1], interval2[1])]

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # insert interval such that no overlapping intervals
        # merge if needed

        # [1,3] [4,6].   [2,5]
        # compare start of new interval to start of old interval.
        # if start of new > start of old AND end of new < start of next interval:
        # we can insert without merging intervals

        # [1,3] [5,6] [2,4]
        # if start is less than end we need to marge
        if not intervals:
            return [newInterval]
        # just insert it first
        for i, interval in enumerate(intervals):
            if newInterval[0] < intervals[i][0]: #interval belongs at start of list
                intervals.insert(0, newInterval)
                print(intervals)
                break
            if i + 1 >= len(intervals): # interval belongs at end of list
                intervals.append(newInterval)
                print(intervals)
                break
            # find where to insert
            if intervals[i][0] < newInterval[0] and intervals[i + 1][0] > newInterval[0]:
                intervals.insert(i + 1, newInterval)
                print(intervals)
                break
    
        # now go through and merge if needed
        i = 0
        while i < len(intervals) - 1:
            # [3,7] [8,10] 
            # [1,2] [3,5]
            # overlapping intervals
            if intervals[i+1][0] <= intervals[i][1]:
                # replace
                intervals[i:i+2] = [self.merge(intervals[i], intervals[i + 1])]
            else:
                i += 1
        
        return intervals


        
        