class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # elements of the same colors are sorted togerher and in order
        # in place sorting reminds me of merge sort
        # o(1) space and o(nlogn) time complexity
        # recursivly split a list till the list is one element
        # then sort in place by comparing two lists and using two pointers to do so

        count = [0] * 3
        for num in nums:
            count[num] += 1

        index = 0
        for i in range(3):
            while count[i]:
                count[i] -= 1
                nums[index] = i
                index += 1
            
        