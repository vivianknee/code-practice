class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        hashS = dict()
        hashT = dict()

        for ch in s:
            hashS[ch] = hashS.get(ch, 0) + 1

        for ch in t:
            hashT[ch] = hashT.get(ch, 0) + 1

        return hashS == hashT

        