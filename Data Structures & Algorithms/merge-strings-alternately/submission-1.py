class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # this is a question involving pointers
        # keep track of two pointers
        # on handling word1 and one for word2
        # both pointers will start at index 0
        # iterate over the len of the shorter word and alternativly append char 
        # once we reach the end of the shorter word, append reamins of the word2

        p1 = p2 = 0
        res = []

        # this code shud handle word1 being longer
        while p1 < len(word1):
            res.append(word1[p1])
            if p2 < len(word2):
                res.append(word2[p2])
                p2 += 1
            p1 += 1
            
        # at this point word1 or word2 shud be exaushted
        while p2 < len(word2):
            res.append(word2[p2])
            p2 += 1
        
        return "".join(res)

        # abcd and pq.  apbqcd

