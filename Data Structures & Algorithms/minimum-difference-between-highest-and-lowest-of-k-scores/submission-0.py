class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        # fixed subarray of k
        # we want to get the min score of the subarray. can use abs value for thi

        # intialize a window of size k
        # keep track of the min score and max score of the subarray
        # take the abs diff and append to a temp res

        # iterate over the remaining part of the array which is k to len(nums)
        # do the same thing
        # decrease window size when k is exceeded

        imin = float('inf')
        imax = float('-inf')
        nums.sort()
        for i in range(k):
            imin = min(imin, nums[i])
            imax = max(imax, nums[i])

        res = imax - imin # get the diff between max and min for first window
        print(res)

        l = 0
        for r in range(k, len(nums)):
            if (r-l+1) > k:
                l += 1
            # how to keep track of max and min
            imax = nums[r]
            imin = nums[l]
            res = min((imax - imin), res)
        
        return res
        
            