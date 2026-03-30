class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        # all even go in the beginning
        # odd go at the end
        # order of ints dont matter
        # in order to determine odd or even, we can use %
        # 0 is even and 1 is odd after using % on any int
        # two pointer, one end and one beginning
        # detertmine if both are odd or even
        # cases
            # left even, right odd : do nothing, increase left pointer
            # left even, right even: increase left pointer
            # left odd, right even: swap values, increase and decrease pointers
            # left odd, right odd: decrease right pointer

        l = 0 
        r = len(nums) - 1
        
        while l < r:
            left = nums[l]%2
            right = nums[r]%2
            
            if left == 1 and right == 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
            elif left == 0:
                l += 1
            else: # left is odd AND right is odd
                r -= 1
        
        return nums
