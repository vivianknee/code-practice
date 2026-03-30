import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []
        for num in nums:
            self.add(num)
        

    def add(self, val: int) -> int:
        # checking for kth largest int in the heap
        # check that there are enough values in the heap
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        # check if the value we are adding is larger than the kth largest value. in this case replace
        elif val > self.heap[0]:
            heapq.heappop(self.heap)
            heapq.heappush(self.heap, val)

        # heaps automatically ensure that the parent is always smaller than the child
        # so by using a heap, we somewhat ensure that the stream is in order numerically
        # return that value
        return self.heap[0]
