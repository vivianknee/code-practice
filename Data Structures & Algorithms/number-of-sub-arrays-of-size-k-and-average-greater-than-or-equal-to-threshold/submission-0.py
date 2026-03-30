class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        # fixed window of size k
        # each time we check the avg of the subarry and determine if it violates the condition
        res = 0
        total = 0
        for i in range(k):
            total += arr[i]
        if total // k >= threshold:
            res += 1
        
        l = 0
        for r in range(k, len(arr)):
            # shrink window if we exceed k
            if (r - l + 1) > k:
                total -= arr[l]
                l += 1
            # otherwise add incoming values and test condition
            total += arr[r]
            if total // k >= threshold:
                res += 1
        return res

        # run through an example
        # 2 2 2 2 5 5 5 8 k = 3 th = 4
        # 222 2 < 4 no
        # 222 2 < 4 no
        # 225 3 < 4 no
        # 255 4=4 yes
        # 555 yes
        # 558 yes
        # return 3