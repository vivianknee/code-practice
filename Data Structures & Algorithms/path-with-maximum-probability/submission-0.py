class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        # each index represents an edge. start node --> end node
        # each edge has a correspoding success traversal rate
        # find the path with the max prob of succes
        # provided with start and end
        # use a max heap which we can simulate with neg numbers in a min heap
        # we wil create an adjacency list pairing start nodes to end nodes for every single node
        # path means we cant travers the same edge twice --> use a set to keep track of traveresed edges

        # initalize our maxheap with our starting position and the probability which we can just 
        # set to 0 for intial
        # we will iterate over the potential edges and append to our max heap. 
        # everytime we pop, we pop the value that has the max probability
        # what are we appending to the max heap? [probability, destination]
        # probability will be an accumulating value
        # we return probability which shud be the max by the time the heap is empty

        # maps source to destination for each source and the prob for that destination
        adjList = defaultdict(list)
        for i, (start, end) in enumerate(edges):
            adjList[start].append((end, succProb[i]))
            adjList[end].append((start, succProb[i]))
        print(adjList)
    
        visit = set() # holds nodes that we have visited
        maxH = [[-1,start_node]]
        while maxH:
            prob, start = heapq.heappop(maxH)
            # reached our destination
            if start == end_node:
                return -prob

            if start in visit:
                continue
            visit.add(start)

            for nei, nei_prob in adjList[start]:
                if nei not in visit:
                    heapq.heappush(maxH, (prob * nei_prob, nei))
        
        # if we never reach our desintaion:
        return 0








