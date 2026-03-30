class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # want to find the route that has minimum effor
        # each value in heights represents the height at that row and col
        # effort is the max abs diff in heights between
        # two consectuive cells of the route aka depends on where i head next

        # djikstras solution
        rows, cols = len(heights), len(heights[0])
        minHeap = [[0,0,0]] # max absolute diff, r, c
        visit = set()
        directions = [[0,1], [1,0], [0,-1], [-1,0]]

        while minHeap:
            diff,r,c = heapq.heappop(minHeap)

            if (r,c) in visit:
                continue
            visit.add((r,c))

            if (r,c) == (rows-1, cols-1):
                return diff # this will be max diff
            
            for dr, dc in directions:
                newr, newc = r + dr, c + dc

                if (newr,newc) in visit or newr < 0 or newr >= len(heights) or newc < 0 or newc >= len(heights[0]):
                    continue
                newDiff = max(diff, abs(heights[r][c] - heights[newr][newc]))
                heapq.heappush(minHeap, [newDiff, newr, newc])

        return 0









        # backtracking solution 
        # we want to try every potential path to get the minimum
        # we want to do depth first search start at the position [0][0] in heights
        # recursive function taking pos in heights and a visited set
            # base case which is being out of bounds OR if we are visiting a pos we have 
            # already visited in that recursive call
            # array of directions
            # iterate over this array of directions
            # before calling a new recurive cal
            # calculate the effor and add it to a variable
            # at the end of each return, we want to update a minimum
        # visited = set()
        # INF = float('inf')
        # directions = [[0,1], [1,0], [0,-1], [-1,0]]

        # # i want this function to return the min effort after traversing each path
        # def dfs(x, y, currentMax):
        #     # base cases
        #     # we reached our destination, return the current max
        #     if x == len(heights) - 1 and y == len(heights[0]) - 1:
        #         return currentMax
            
        #     # if it passes those edge cases, we can add the coordinates to visited
        #     visited.add((x,y))
        #     res = INF
        #     for d in directions:
        #         x_new = x + d[0]
        #         y_new = y + d[1]
        #         # out of bounds, pick a different direction
        #         if (x_new,y_new) in visited or x_new < 0 or x_new >= len(heights) or y_new < 0 or y_new >= len(heights[0]):
        #             continue # no potential path so no effort used

        #         newMax = max(currentMax, abs(heights[x_new][y_new] - heights[x][y]))
        #         res = min(res, dfs(x_new, y_new, newMax))

        #     visited.remove((x, y))
        #     return res
        
        # return dfs(0,0,0)

        

            
















