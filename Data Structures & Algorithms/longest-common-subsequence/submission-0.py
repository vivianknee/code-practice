class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # lcs need not be conitguous, only in order

        # identify which text is smaller and compare smaller to larger
        # for len(text1) + 1 rows, 
        dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]
        
        # start at bottom corner
        for i in range(len(text1) - 1, -1, -1): # bottom row
            for j in range(len(text2) - 1, -1, -1): #bottom col
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])
        
        return dp[0][0]



            




            
            
