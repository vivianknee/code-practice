"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # sort sort sort!
        intervals.sort(key=lambda x: x.start) # auto sorts by start times
        # anaylze edge cases for conflicting meetings
        # (0,30) (5,10) # starts within and ends before
        # (0,30) (5,35) # starts within, ends after
        if not intervals:
            return True
            
        prevEnd = intervals[0].end
        print(prevEnd)
        for i in intervals[1:]:
            if i.start >= prevEnd: # no overlap:
                prevEnd = i.end
            else: # overlap
                return False
        
        return True







                