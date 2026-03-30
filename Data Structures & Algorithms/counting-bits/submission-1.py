class Solution:
    # dp solution
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        offset = 1

        # index 0 is always 0, can be skipped
        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
            
            dp[i] = 1 + dp[i - offset]
        
        return dp



    # o(nlogn)
    # def numOfOnes(self, n):
    #         count = 0

    #         for i in range(31, -1, -1):
    #             num = n >> i # shift right i bits
    #             if num & 1 == 1:
    #                 count += 1
            
    #         return count

    # def countBits(self, n: int) -> List[int]:
    #     res = []
    #     for i in range(n + 1):
    #         res.append(self.numOfOnes(i))
        
    #     return res
