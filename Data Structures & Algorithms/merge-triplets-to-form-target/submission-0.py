class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # to find our target , we can perform the oepration
        # we dont want to lose our target if it gets overriden by the operation
        # so sorting the triplets might be wise
        # sort it in ascending order
        # then we want to see if the first number in the triplet is less than or equal to
        # the coresponding target
        # if equal move onto next number in triplet
        # if less, move a right pointer forward and check first num
        # repeat for all
        found = [False, False, False]
        for i, j, k in triplets:
            if i > target[0] or j > target[1] or k > target[2]:
                continue
            
            if i == target[0]:
                found[0] = True
            if j == target[1]:
                found[1] = True
            if k == target[2]:
                found[2] = True
        
        return all(found)
            

