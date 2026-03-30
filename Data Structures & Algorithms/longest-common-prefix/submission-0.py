class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        #use one word as ref, in this case the first word
        for i in range(len(strs[0])):
            for s in strs:
                #first condition checks that the string is len 0 
                if i == len(s) or s[i] != strs[0][i]:
                    return prefix 
            prefix += strs[0][i]

        return prefix 


        