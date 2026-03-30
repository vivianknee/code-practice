class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        # fixed sliding window of size k
        # set up the intiial window to analyze
        whites = 0
        res = float('inf')
        for i in range(k):
            if blocks[i] == 'W':
                whites += 1
        res = whites
        
        # add new element and remove old
        l = 0
        for r in range(k, len(blocks)):
            if blocks[l] == 'W':
                whites -= 1
            if blocks[r] == 'W':
                whites += 1
            res = min(res, whites)
            l += 1
        
        return res