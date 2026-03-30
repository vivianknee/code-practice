class Solution:
    def maxSumDistinctTriplet(self, x: List[int], y: List[int]) -> int:
        # iterating over x, we want to examine each possibility where the values at the indices are diff
        # each time find a possibility, we want to update a max value of the y values
        # finding each possiblity brute force would be very costly
        # adj list
        # for each unique value in x, we will have a list of the values in y that corsepond to it
        # x = [1,2,1,3,2], y = [5,3,4,6,2]
        # 1 : 5, 4
        # 2 : 3, 2
        # 3 : 6
        # we want the max sum over 3 numbers so we iterate over this adjList, adding the max of the
        # values to a sum result
        # this result shud contain the max
        # if the len of the adjlist is < 3 this means we have less than 3 distinct values and the
        # solution is automatically false

        adjList = defaultdict(list)
        for num, val in zip(x, y):
            adjList[num].append(val)
        print(adjList)

        if len(adjList) < 3:
            return -1
        
        total = []
        # there could be MORE than three distinct values
        # instead lets get an array of all maxes and from these, choose the largest three
        for number, values in adjList.items():
            max_num = float('-inf')
            for val in values:
                max_num = max(max_num, val)
            total.append(max_num)
        
        total.sort(reverse=True)
        return sum(total[:3])










