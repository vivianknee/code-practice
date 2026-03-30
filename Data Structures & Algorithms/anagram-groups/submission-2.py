class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = defaultdict(list) #map letter count to list of anagrams

        for word in strs:
            count = [0]*26 #represents every letter in alphabet
            for c in word:
                count[ord(c)-ord("a")] += 1 #counting how many of each character
            
            res[tuple(count)].append(word)

        return list(res.values())

        