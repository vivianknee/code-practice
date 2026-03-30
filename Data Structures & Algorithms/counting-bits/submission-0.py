class Solution:
    def numOfOnes(self, n):
            count = 0

            for i in range(31, -1, -1):
                num = n >> i # shift right i bits
                if num & 1 == 1:
                    count += 1
            
            return count

    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n + 1):
            res.append(self.numOfOnes(i))
        
        return res
