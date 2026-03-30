class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # smallest space complexity possible
        # involves sorting in place
        # merge sort and quicksort and heap sort are nlogn
        # we will go through the array nums and append each num to a min heap
        # adding to a min heap auto sorts where the min is the root of the heap.
        # popleft on the min heap and 
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


        