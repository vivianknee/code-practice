class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #check that the number in nums2 is in nums1. 
        #if so, check items only to the right of that num in nums2
        #return the first num greater than that num, else return -1

        nums1Idx = {}

        #create a hashmap of index value pairs of num1
        for i,val in enumerate(nums1):
            nums1Idx[val] = i

        #initialize an array of -1
        res = [-1] * len(nums1)

        stack = []
        for i in range(len(nums2)):
            curr = nums2[i]
            while stack and curr > stack[-1]:
                val = stack.pop()
                idx = nums1Idx[val]
                res[idx] = curr
            if curr in nums1Idx:
                stack.append(curr)
        return res