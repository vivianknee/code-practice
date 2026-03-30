class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(path):
            # base case is if the permutation or path is the same length as nums. 
            # in this case we have reached the leaf node, so append to result
            if len(path) == len(nums):
                res.append(path.copy())
                return
            
            # for each num in nums, we want to do this recursive process on it
            for num in nums:
                # cant have two of the same num in the perm
                # if the num is already in there, we continue
                if num in path:
                    continue
                # if its not in there, append it to the current path
                path.append(num)
                # recursivley run the function on the new path
                backtrack(path)
                # at the same time, run the function on the backtracking step
                path.pop()
            
        backtrack([])
        return res



        