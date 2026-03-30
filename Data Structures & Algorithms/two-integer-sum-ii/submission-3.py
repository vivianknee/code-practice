class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # left and right pointer, left at 0, right at end of numbers
        # since the arr numbers is ordered
        # if the sum of the two pointers are > target, we move right down and if 
        # sum < target, we can move left up
        # while l < r, we havent traveresed every posibility
        # each time we find a target mach, we append that left and right values to a result

        # numbers = [1,2,3,4], target = 3
        l = 0
        r = len(numbers) - 1
        res = []
        while l < r:
            twoSum = numbers[l] + numbers[r]
            if twoSum > target:
                r -= 1
            elif twoSum < target:
                l += 1
            else: # match! l < r append l first
                res.append(l+1)
                res.append(r+1)
                l += 1
                r -= 1
        
        return res

        
        


