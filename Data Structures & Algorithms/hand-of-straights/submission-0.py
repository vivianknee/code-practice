class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # hand arr holds card values
        # i want to see if i can arrage all cards in increasing by 1 order
        # in groups of groupsize

        # we can count the number of each value in hand
        # iterate over this list creating groupsize groups till each value in the dict 
        # has freq 0

        adjList = {}
        for val in hand:
            if val in adjList:
                adjList[val] += 1
            else:
                adjList[val] = 1
        sorted_keys = sorted(adjList.keys())

        for start in sorted_keys:
            while adjList[start] > 0:  # form groups starting here
                # Try to form one group: start, start+1, ..., start+groupSize-1
                for i in range(groupSize):
                    card = start + i
                    if adjList.get(card, 0) == 0:
                        return False  # missing consecutive card!
                    adjList[card] -= 1
        
        return True




        
        if sum(adjList.values()) == 0:
            return True
        else:
            return False
            