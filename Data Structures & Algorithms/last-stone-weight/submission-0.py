class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # given an array of stone weights
        # choose the two heaviest stones --> smash them together
        # x == y --> stones destroyed
        # x < y --> stone x is destroyed and vice versa. new stone weight is y - x
        # continue this until one stone remains, aka while loop until len of stones is 1

        while len(stones) > 1:
            stones.sort()
            x = stones.pop()
            y = stones.pop()

            if x < y:
                stones.append(y - x)
            else:
                stones.append(x - y)
            
            # if the two stones weigh the same, append nothing, rocks destroyed
        if not stones:
            return 0
        else:
            return stones[0] 
        