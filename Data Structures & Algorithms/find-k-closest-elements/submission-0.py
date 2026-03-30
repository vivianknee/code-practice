class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # return k closest ints to x in the array
        # might be wise to sort the array
        # sliding window problem
        # we want to keep the window the size of k
        # test the condition of the right int to that of the left int

        n = len(arr)
        idx = 0
        for i in range(1, n):
            if abs(x - arr[idx]) > abs(x - arr[i]):
                idx = i

        res = [arr[idx]]
        l, r = idx - 1, idx + 1

        while len(res) < k:
            if l >= 0 and r < n:
                if abs(x - arr[l]) <= abs(x - arr[r]):
                    res.append(arr[l])
                    l -= 1
                else:
                    res.append(arr[r])
                    r += 1
            elif l >= 0:
                res.append(arr[l])
                l -= 1
            elif r < n:
                res.append(arr[r])
                r += 1

        return sorted(res)

        