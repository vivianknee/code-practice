class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # min cost 
        # djikstras algorithim
        # min heap to continuosly pop the nearest point by distance
        # i can order the coordinates by x and y since logically
        # min cost would mean the points are lined up in a way so that we dont travel backwards
        # i want to check every distance
        # min heap needs to store the cost to connect, and the point index


        # start at any point --> start at the first point in points
        # append
        N = len(points)
        adj = {i:[] for i in range(N)}
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]
                dist = abs(x1-x2) + abs(y2-y1)
                adj[i].append([dist, j])
                adj[j].append([dist, i])
        
        res = 0
        visit = set()
        minHeap = [[0,0]] # cost , point 0 (not coordinate 0)
        while len(visit) < N:
            cost, i = heapq.heappop(minHeap)
            if i in visit:
                continue
            res += cost
            visit.add(i)
            for neiCost, nei in adj[i]:
                if nei not in visit:
                    heapq.heappush(minHeap, [neiCost, nei])
        
        return res
            


        



