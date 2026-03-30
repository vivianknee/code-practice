class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for ch in s:
            if ch in pairs:  
                if not stack or stack[-1] != pairs[ch]: #check that the stack isnt empty or if the top of the stack equals the corresponding openening bracket
                    return False
                stack.pop()
            else:  # opening bracket
                stack.append(ch)
            print(stack)

        if len(stack) == 0:
            return True
        else:
            return False