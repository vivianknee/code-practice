class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        # min heap
        # python doesnt have max heap, so we will simulate a max heap with a min heap
        # negating all hte values in the heap
        # kth largest element to be the root, and we pop the root each time we call the function
        # we want to populate the heap till its size k

        heap = []

        for num in nums:
            # append values to the heap till the length is k
            if len(heap) < k:
                # append the negative to simulate a max heap
                heapq.heappush(heap, num)
            # root is 5 and i want to add the num 8.
            # 8 wud be greater than 5
            # so i want to replace when the new value is greater than the min
            elif num > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, num)
        
        return heap[0]

