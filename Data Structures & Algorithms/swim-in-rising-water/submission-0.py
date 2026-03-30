class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # each pos in grid represents the elevation
        # at time t, water of entire grid is t
        # you can swim if the cur square and adj sqaure is <= water level
        # return min time to reach bottom right square from top right

        # starting at (0,0)
        # keep track of time t, starts at 0
        # hold onto a minHeap (time, x, y)
        # check horizontal and vertical directions
            # can we swim? if values at curSquare and adjSquare <= time, we can continue
            # append(time + 1, newx, newy)
        # every iteration of checking the minheap
            # check if we have reached the bottom right
            # in this case, we return time. 
            # because in this djikstras greedy, the time accumulates
            # we dont want to go back to squares we have already visited so have a set
        
        visit = set()
        minH = [(grid[0][0],0,0)]
        directions = [[0,1], [0,-1], [1,0], [-1,0]]
        rows, cols = len(grid), len(grid[0])

        while minH:
            time, x, y = heapq.heappop(minH)

            if (x,y) in visit:
                continue
            visit.add((x,y))

            # we reached the bottom right square
            # there is always a way to get to the bottom right square so only need to return here
            if x == rows-1 and y == cols-1:
                return time

            for dx, dy in directions:
                newX, newY = x + dx, y + dy
                # dead end
                if (newX, newY) in visit or newX < 0 or newY < 0 or newX > rows-1 or newY > cols-1:
                    continue 

                # new time is the max of cur or adj
                newTime = max(time, grid[newX][newY])
                # minheap will make sure we pop the lowest time first
                heapq.heappush(minH, (newTime, newX, newY))





