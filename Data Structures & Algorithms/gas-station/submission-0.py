class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # return starting gas station index so you can travel around the circuit once(going right

        for i in range(len(gas)):
            cycle = c = g = 0
            station = i
            while cycle < len(gas):
                c = cost[station] # update cost
                g += gas[station] # add gas from new station
                
                if g < c:
                    break

                g -= c # update gas
                if station == len(gas) - 1:
                    station = 0
                else:
                    station += 1 

                cycle += 1 # keep track of if we made a full circle
            
            if cycle == len(gas):
                return station
        
        return -1
            

