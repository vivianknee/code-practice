class Solution:
    def checkValidString(self, s: str) -> bool:
        # use a stack
        # if the char is '(' we append to the stack
        # if the char is ')' we pop from the stack
        # if the char is "*" we need to see what the last thing in the stack was
            # if the last thing in the stack is (, we can pop it
            # otherwise it adds nothing, so we can treat it as nothing and continue
        leftmin, leftmax = 0,0
        for c in s:
            if c == "(":
                leftmin, leftmax = leftmin + 1, leftmax + 1
            elif c == ")":
                leftmin, leftmax = leftmin - 1, leftmax - 1
            else:
                leftmin, leftmax = leftmin - 1, leftmax + 1
            if leftmax < 0:
                return False
            if leftmin < 0:
                leftmin = 0

        return leftmin == 0

        # s="("
        # stack = [)]