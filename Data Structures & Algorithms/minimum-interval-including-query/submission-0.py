class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # we want the len of shortest interval containing the num in queries

        # create an adj list of num in queries and intervals that contain it
        q = 0
        adjList = defaultdict(list)
        while q < len(queries):
            for x, y in intervals:
                if x <= queries[q] <= y:
                    adjList[queries[q]].append((x,y))
            q += 1
        
        res = []
        # for each query in the adjlist, i want to get the len of the interval that is the smallest
        # append that smallest interval to res
        for q in queries:
            min_len = float('inf')
            if q not in adjList:
                res.append(-1)
                continue
            for interval in adjList[q]:
                min_len = min(min_len, interval[1]-interval[0] + 1)
            res.append(min_len)
        
        return res



