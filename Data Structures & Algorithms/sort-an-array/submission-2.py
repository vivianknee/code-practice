class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # smallest space complexity possible
        # involves sorting in place
        # merge sort and quicksort and heap sort are nlogn
        # we will go through the array nums and append each num to a min heap
        # adding to a min heap auto sorts where the min is the root of the heap.
        # popleft on the min heap and 
        heapq.heapify(nums)

        res = []
        while nums:
            res.append(heapq.heappop(nums))
        
        return res