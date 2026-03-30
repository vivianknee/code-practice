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

        def merge(arr, L, M, R):
            left, right = arr[L:M+1], arr[M+1:R+1]
            i, j, k = L, 0, 0

            while j < len(left) and k < len(right):
                if left[j] <= right[k]:
                    arr[i] = left[j]
                    j += 1
                else:
                    arr[i] = right[k]
                    k += 1
                i += 1
            while  j < len(left):
                nums[i] = left[j]
                j += 1
                i += 1
            while  j < len(right):
                nums[i] = right[k]
                k += 1
                i += 1


        def mergeSort(arr, l, r):
            if l == r:
                return arr
            
            m = (l+r) // 2
            mergeSort(arr, l, m)
            mergeSort(arr, m + 1, r)
            merge(arr, l, m, r)
            return arr
        
        return mergeSort(nums, 0, len(nums) - 1)
            
        