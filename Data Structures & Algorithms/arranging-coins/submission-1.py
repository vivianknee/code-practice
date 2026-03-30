class Solution:
    def arrangeCoins(self, n: int) -> int:
        # ith row has i coins
        # row 0 has 0, row 1 has 1, etc
        # last stair case may be incomplete
        # return number of complete staircases
        # you have n coins


        # brute force
        # coins = n
        # i = 0 to represent row we are at
        # while coins > 0:
        # perform operations
            # coins -= i
            # if coins > 0:
                # increment to next row
        
        coins = n
        i = 0
        while coins > 0:
            remains = coins - i
            if remains >= i + 1:
                coins = remains
                i += 1
            else:
                return i

        return i