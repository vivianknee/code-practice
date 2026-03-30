class Solution:
    def numDecodings(self, s: str) -> int:
        # cant have leading zeros
        # number can be decoded from a 1 or 2 digit num

        # if a 2 digit num < 26, it can auto be decoded in two ways
        # start at first digit
        # two choices
            # if the curr digit is not a zero
            # we can decode the curr digit
            # we can decode the curr digit and the next as one digit
        
        ways = 0
        def dfs(i):
            if i == len(s): # reached the end
                return 1

            if s[i] == '0': # leading zero
                return 0

            # take one digit
            ways = dfs(i + 1)
                
            # take two digits (if valid)
            if i + 1 < len(s) and int(s[i:i+2]) <= 26:
                ways += dfs(i + 2)
            
            return ways

        return dfs(0)