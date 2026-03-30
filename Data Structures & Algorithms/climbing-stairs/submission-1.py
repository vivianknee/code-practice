class Solution:
    def climbStairs(self, n: int) -> int:
        # n represents number of steps to reach top of a staircase
        # climb with either 1 or 2 steps at a time
        # return # of ways to climb to top of the staircase
       
        one, two = 1, 1
        for i in range(n-1):
            temp = one
            one = one + two
            two = temp

        return one











        # choose either 1 or 2 at each step
        # if we exceed the target n, we BACKTRACK , subtract, and try the other value
        # self.num_of_ways = 0
        # # curr represents the total at this point
        # def backtrack(curr):
        #     if curr == n:
        #         self.num_of_ways += 1
        #         return
            
        #     if curr > n:
        #         return
            
        #     backtrack(curr + 2)
        #     backtrack(curr + 1)

        # # main function
        # # call backtrack and recursivly add to an int num_of_ways
        # # return num_of_ways

        # backtrack(0)
        # return self.num_of_ways

        # walk through this code:
            # n = 2
            # back(0) --> back(2) --> numways = 1 --> return
            # back(1) --> back(3) --> return
            # back(1) --> back(2) --> numways = 2 --> return
            # reached end --> exit
        # extremely inefficient o(2^n)