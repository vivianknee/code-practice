class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # given a 2d array of points
        # given an int k
        # return the k closest points to the origin
        # use the distance formula
        # can be returned in any order

        # initialize a heap to store distance
        # store the k smallest distances so this is a min heap o(logn)
        # iterate through points, and check if we get a smaller distance at each iteration
        # compare that with the root value in the heap, replace if its smaller. 
        # we also want to ensure that the heap stays the len(k)
        heap = []
        for x,y in points:
            # calculate the distance
            distance = math.sqrt((x - 0)**2 + (y - 0)**2)

            # if the len of the heap is less than k, append distance values to the heap
            if len(heap) < k:
                heapq.heappush(heap, (-distance, [x, y]))
            elif -distance > heap[0][0]:
                heapq.heappop(heap)
                heapq.heappush(heap, (-distance, [x, y]))
        
        result = []
        for dist, point in heap:
            result.append(point)
        return result

            

            