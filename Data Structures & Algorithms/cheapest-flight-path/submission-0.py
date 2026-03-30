class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # flights contains start airport, end airport, and cost of travel
        # each flight is one way --> can only be used once
        # cheapest price to reach destination --> djikstras algorithm
        # adj list price of travel : (start, end)
        # visit set() so i dont travel backwards since we can only use each flight once
        # minheap to calculate the min cost. append to the min heap (cost, destination)

        # adj list shud contain each src : (cost, dst)
        adjList = defaultdict(list)
        for start, end, price in flights:
            adjList[start].append((price, end))
        
        visited = {}
        res = 0
        minH = [(0, src, 0)] # starting src and starting cost and stops used

        while minH:
            cost, node, stops = heapq.heappop(minH)
            if node == dst:
                return cost
            
            # Skip if visited with fewer/equal stops
            if node in visited and visited[node] <= stops:
                continue
            visited[node] = stops

            if stops <= k:
                for price, nei in adjList[node]:
                    heapq.heappush(minH, (cost + price, nei, stops + 1))
        
        return -1





