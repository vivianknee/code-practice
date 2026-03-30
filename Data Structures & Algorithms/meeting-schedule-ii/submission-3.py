"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])
        res, count = 0, 0
        s, e = 0, 0
        while s < len(intervals):
            # new meetings are starting
            if start[s] < end[e]:
                s += 1
                count += 1
            # a meeting ended
            else:
                e += 1
                count -= 1
            # res is max because at any point in time there were two meetings running in parallel
            # means we need two rooms
            res = max(res, count)
        
        return res
        
