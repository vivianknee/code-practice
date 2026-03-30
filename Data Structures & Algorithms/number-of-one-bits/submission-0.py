class Solution:
    def hammingWeight(self, n: int) -> int:
        # for i in range of 32 bits
        # shift the bits by i each time, starting backwards
        # shift last bit to front
        # perform and operation with 1 on it
        # 1 means its a 1, otherwise its a 0

        count = 0

        for i in range(31, -1, -1):
            num = n >> i # shift right i bits
            if num & 1 == 1:
                count += 1
        
        return count