class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # bottom up
        # start with the first char in the word
        # dp = [False] * len(s) 
        # dp[0] = False

        # for i in range(1, len(s)):
        #     for word in wordDict:
        #         # can this word go into the curr string?
        #         if s[0:i] == word:
        #             dp[i] = True
                
        # return dp[-1]

        # top down - memoization
        memo = {}
    
        def dfs(i):
            if i == len(s):
                return True
            
            if i in memo:  # ADD: check cache
                return memo[i]
            
            for word in wordDict:
                if s[i:i+len(word)] == word:
                    if dfs(i + len(word)):
                        memo[i] = True  # ADD: cache result
                        return True
            
            memo[i] = False  # ADD: cache result
            return False
        
        return dfs(0)


        # naive recurison
        # def dfs(i):
        #     if i == len(s): # reached the end of the word
        #         return True
            
        #     for word in wordDict:
        #         if s[i:i+len(word)] == word: # check that s starts with word
        #             if dfs(i + len(word)):
        #                 return True
            
        #     return False
        
        # return dfs(0)
