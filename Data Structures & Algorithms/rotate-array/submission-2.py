class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # rotate by k steps to the right in place
        # nums = [1,2,3,4,5,6,7,8], k = 4 --> [5,6,7,8,1,2,3,4]
        # new index is curr index + 4
        # keep replacing till we surpass the lengthof the list
        # then go back to next iteration
        # nums = [1,2,3,4,5,6,7,8], k = 4 
        # first iteration. while we not reached end
        # 0 --> 4 1 replace 5. store 5 in a temp variable put 1 where 5 shud be
        k = k % len(nums)
        l,r = 0, len(nums) -1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l , r = l + 1, r - 1
        
        l,r = 0 , k -1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l , r = l + 1, r - 1
        
        l,r = k, len(nums) -1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l , r = l + 1, r - 1

