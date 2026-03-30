class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = []
        for i in range(len(words)):
            for j in range(len(words)):
                if i == j:
                    continue #if i is j, ur comparing the word to itself and thats pointless
                if words[i] in words[j]:
                    res.append(words[i])
                    break
        return res