class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # bottom up
        # start with the first char in the word
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(s) + 1):
            for word in wordDict:
                # can this word go into the curr string?
                if i >= len(word) and s[i-len(word):i] == word:
                    if dp[i - len(word)]:
                        dp[i] = True
                        break
        return dp[-1]
                
        # return dp[-1]

        # top down - memoization
        # memo = {}
    
        # def dfs(i):
        #     if i == len(s):
        #         return True
            
        #     if i in memo:  # ADD: check cache
        #         return memo[i]
            
        #     for word in wordDict:
        #         if s[i:i+len(word)] == word:
        #             if dfs(i + len(word)):
        #                 memo[i] = True  # ADD: cache result
        #                 return True
            
        #     memo[i] = False  # ADD: cache result
        #     return False
        
        # return dfs(0)


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
