class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # fruits is an array of types of fruit trees
        # two baskets, each can hold an unlimited amount of fruit of ONE type
        # can start at ANY tree in which u need to take that fruit
        # stop when u can no longer store any fruits
        # return max fruits you can pick

        # dynamic sliding window since each subarray can be a diff size
        # dictionary to store fruit type and their frequencies
        # when the len of the dict exceeds two, means wer found a third distinct fruit type
        # we can hold that so the iteration starting at that tree stops.
        # increment left pointer by 1 each time we stop and restart to test a new starting point tree
        # remove from the dictionary as necessary

        seen = {}
        l = 0
        res = float('-inf')
        for r in range(len(fruits)):
            fruitType = fruits[r]
            if fruitType in seen:
                seen[fruitType] += 1
            else:
                seen[fruitType] = 1
            
            while len(seen) > 2: 
                leftFruit = fruits[l]
                seen[leftFruit] -= 1
                if seen[leftFruit] == 0:
                    del seen[leftFruit]
                l += 1
            res = max(res, sum(seen.values()))
        
        return res







