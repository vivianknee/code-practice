class Solution:
    def compare(self, interval1, interval2):
        if interval2[0] < interval1[0]:
            interval1, interval2 = interval2, interval1
        
        x1, y1 = interval1[0], interval1[1]
        x2, y2 = interval2[0], interval2[1]
        
        if x2 <= y1:  # overlap
            return [[x1, max(y1, y2)]]
        else:
            return [[x1, y1], [x2, y2]]

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
    
        intervals.sort(key=lambda x: x[0])  # just sort by start
        
        res = [intervals[0]]
        
        for i in range(1, len(intervals)):
            merged = self.compare(res[-1], intervals[i])
            if len(merged) == 1:
                res[-1] = merged[0]  # replace with merged interval
            else:
                res.append(intervals[i])  # no merge, add new
        
        return res