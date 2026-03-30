class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        # each item is the # of customers entering and leaving at that min. 
        # owner is either grumpy 1 or not 0 at each min
        # the owner can be not angry for minutes minutes
        # ideally we want to create a subarray within grumpy such that there is the most 
        # consecutive zeros (not grumpy)
        # we can do a sliding window over the grumpy array and treat minutes as the
        # size of the window
        # once we encounter enough ones such that its greater than the window size, we can shrink by 1
        # to test a new subarray
        # as we do this, we are updating a max for the amount of satisfied customers

        superpower = 0
        currRes = 0
        for i in range(len(grumpy)):
            if superpower < minutes:
                # increment super power regardless
                superpower += 1
                currRes += customers[i]
                continue # continue as to not double count
                
            # superpower is used up, increment remaining list
            if grumpy[i] == 0:
                currRes += customers[i]
        res = currRes
        print(res)
        
        l = 0
        for r in range(minutes, len(grumpy)):
            # already calculated total satisfied customer for minutes being first interval
            # test the rest by subtracting the left IF grumpy is 1 there
            # because had it been zero, it wudv been counted regardless
            if (r - l + 1) > minutes:
                if grumpy[l] == 1:
                    currRes -= customers[l]
                l += 1
            # to our total, we only add the current r IF we hadnt added it before
            # so we test if at the index r, we are at a 1
            if grumpy[r] == 1:
                currRes += customers[r]
            
            # update the res each time to keep track of the max
            res = max(res, currRes)

        return res







