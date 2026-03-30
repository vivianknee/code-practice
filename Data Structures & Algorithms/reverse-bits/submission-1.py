class Solution:
    def reverseBits(self, n: int) -> int:
        # reverse the bits
        # or operation with each bit
        res = 0

        for i in range(32):
            bit = (n >> i) & 1 
            res = res | (bit << (31 - i))
        
        return res
        

