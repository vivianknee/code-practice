class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        # each row in costs represents a house to be painted
        # each col represents the color
        # 0 red, 1 green, 2 blue
        # two of the same color cant be next to each other
        # rewrite this in memo!
        memo = {} # house index, prevColor: min cost given the prevColor
        def dfs(row, prevColor): # row is the house, col is the color of the 
            # if we reach the last row, we have painted the last house
            if row == len(costs):
                return 0 # no cost to paint house that doesn't exist
            
            if (row, prevColor) in memo:
                return memo[(row, prevColor)]
            
            curCost = float('inf')
            # iterate over len(costs[row]) --> always 3 options
            for i in range(len(costs[row])):
                if i == prevColor:
                    continue
                # continuously update to curCost or cost at that house + the next row
                curCost = min(curCost, costs[row][i] + dfs(row + 1, i))
            memo[(row, prevColor)] = curCost
            return memo[(row, prevColor)]
        
        return dfs(0, -1)
