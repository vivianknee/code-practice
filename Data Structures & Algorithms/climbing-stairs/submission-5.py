class Solution:
    def climbStairs(self, n: int) -> int:
        # top down - memoization
        # use recursion and memorization
        # load a memo with base cases
        memo = {1:1, 2:2}

        # recursive funciton
        def recursion(x):
            # first check if we have already calculated the answer for x
            if x in memo:
                return memo[x]
            else:
                # calculate for that position
                memo[x] = recursion(x-1) + recursion(x-2)
                return memo[x]
        
        return recursion(n)




        # naive recursion o(2^n) time o(n) space
        # n is the number of steps needed to reach the top of the stair case
        # we can climb either 1 step or 2 steps

        # figure out the base cases first
        # if n = 1, there is 1 way (jump 1 step)
        # if n = 2, there are 2 ways (jump 1 step 2x or jump 2 step)
        # if n == 1:
        #     return 1
        # if n == 2:
        #     return 2
        
        # # every other number, we need to fo recursion to figure out
        # return self.climbStairs(n - 1) + self.climbStairs(n - 2)
        