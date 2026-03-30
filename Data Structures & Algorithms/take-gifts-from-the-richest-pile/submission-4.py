import math
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        # we can do this in place by sorting the array
        # then start iterating at the end of the array since we want the largest value
        # each time we take the square root, that value may no longer be the largest
        # to solve this we shud use a max heap, where each time we pop the largest value, take the squre root
        # add it back to the heap
        heap = []
        for i in range(len(gifts)):
            heapq.heappush(heap, -gifts[i]) # force a max heap. root value or first value guarenteed to be the largest

        for i in range(k):
            new_value = int(math.sqrt(-heapq.heappop(heap)))
            heapq.heappush(heap, -new_value)
        
        return abs(sum(heap))
        
