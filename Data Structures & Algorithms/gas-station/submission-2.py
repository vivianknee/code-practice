class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # greedy O(n) O(1)
        if sum(gas) < sum(cost):
            return -1

        total = 0
        start = 0
        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            total += diff
            if total < 0:
                total = 0
                start = i + 1
        
        return start

        # # brute force O(n^2) O(1)
        # for i in range(len(gas)):
        #     cycle = c = g = 0
        #     station = i
        #     while cycle < len(gas):
        #         c = cost[station] # update cost
        #         g += gas[station] # add gas from new station
                
        #         if g < c:
        #             break

        #         g -= c # update gas
        #         if station == len(gas) - 1:
        #             station = 0
        #         else:
        #             station += 1 

        #         cycle += 1 # keep track of if we made a full circle
            
        #     if cycle == len(gas):
        #         return station
        
        # return -1

