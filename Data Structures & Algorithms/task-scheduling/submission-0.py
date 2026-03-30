class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # given array of tasks each task is a char from A to Z
        # given an interger n

        # each cycle allows the completion of one task
        # tasks may be completed in any order
        # identical tasks must be seperated by at least n cycles
        # return min number of cycles needed to complete all tasks

        # iterate through the list of tasks
        # get the char by popping from the list
        # continue iteration until list is empty (while list)

        # we want to process the most frequent task first
        # use a hash map to hold the val and its frquency
        hashmap = {}
        for task in tasks:
            if task in hashmap:
                hashmap[task] += 1
            else:
                hashmap[task] = 1
        
        # i want a max heap
        # process the tasks with the greatest freq first
        heap = []
        for freq in hashmap.values():
            heapq.heappush(heap, -freq) # negative value to simulate max heap
        
        cycles = 0
        queue = deque()
        while heap or queue:
            cycles += 1
            if heap:
                # get the freq from the heap by popping
                freq = -heapq.heappop(heap)
                freq -= 1
                # if the freq > 0, add to the cooldown queue
                # de increment value of freq in the heap
                if freq > 0:
                    queue.append((freq, cycles + n))
            if queue and queue[0][1] == cycles:
                freq, _ = queue.popleft()
                heapq.heappush(heap, -freq) 
        
        return cycles

        



        