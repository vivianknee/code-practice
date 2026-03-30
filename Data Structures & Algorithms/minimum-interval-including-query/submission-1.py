class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # we want the len of shortest interval containing the num in queries
        intervals.sort()
        minHeap = []

        res, i = {}, 0
        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                heapq.heappush(minHeap, (r-l+1, r))
                i += 1
            
            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)
                #pop all invalid ones
            res[q] = minHeap[0][0] if minHeap else -1
        
        return [res[q] for q in queries]
















        # create an adj list of num in queries and intervals that contain it
        # # intervals is n and queries is m
        # q = 0
        # adjList = defaultdict(list)
        # while q < len(queries): # o(m * n) for each query, we check each interval
        #     for x, y in intervals:
        #         if x <= queries[q] <= y:
        #             adjList[queries[q]].append((x,y))
        #     q += 1
        
        # res = []
        # # for each query in the adjlist, i want to get the len of the interval that is the smallest
        # # append that smallest interval to res
        # # worst case o(n * m)
        # for q in queries:
        #     min_len = float('inf')
        #     if q not in adjList:
        #         res.append(-1)
        #         continue
        #     for interval in adjList[q]:
        #         min_len = min(min_len, interval[1]-interval[0] + 1)
        #     res.append(min_len)
        
        # return res

        # space o(m + n)
        # time o(m * n)


