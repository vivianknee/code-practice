class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # given an array of stone weights
        # choose the two heaviest stones --> smash them together
        # x == y --> stones destroyed
        # x < y --> stone x is destroyed and vice versa. new stone weight is y - x
        # continue this until one stone remains, aka while loop until len of stones is 1

        # while len(stones) > 1: # O(n-1) at most
        #     stones.sort() # o(nlogn)
        #     x = stones.pop()
        #     y = stones.pop()

        #     if x < y:
        #         stones.append(y - x)
        #     else:
        #         stones.append(x - y)
            
        #     # if the two stones weigh the same, append nothing, rocks destroyed
        # if not stones:
        #     return 0
        # else:
        #     return stones[0] 
        #o(n^2logn) time complexity
        # o(n) space

        # use a max heap!, python only has min heap so multiply values by -1 to get largest value
        # take absolute value
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)

            if second > first: # first = -8 second = -2
                heapq.heappush(stones, first - second)
        
        if not stones:
            return 0
        else:
            return abs(stones[0])
