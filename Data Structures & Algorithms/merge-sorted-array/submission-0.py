class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # two arrays sorted in increasing order
        # m valid elements in nums1 with last n elements being zeros
        # we want to sort in place
        # sorting in place i think of merge sort but this is simpler
        # both provided array are already in sorted order
        # two pointers, one for each array
        # compare nums1[i] to nums2[i], append
        # before we do all this we can replace the zeros

        last = m + n - 1

        while m > 0 and n > 0:
            if nums1[m-1] > nums2[n-1]:
                nums1[last] = nums1[m-1]
                m -= 1
            else:
                nums1[last] = nums2[n-1]
                n -= 1
            last -= 1
        
        # fill nums1 with leftover num2 elements
        while n > 0:
            nums1[last] = nums2[n-1]
            n, last = n - 1, last - 1







