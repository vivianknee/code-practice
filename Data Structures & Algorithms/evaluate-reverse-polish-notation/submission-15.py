class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        numStack = []
        operators = {"+", "-", "/", "*"}

        for token in tokens:
            if token not in operators:
                numStack.append(int(token))
            else:
                second = numStack.pop()
                first = numStack.pop()
                if token == '+':
                    res = first + second
                elif token == '-':
                    res = first - second
                elif token == '*':
                    res = first * second
                else:  # division
                    res = int(first / second)  # truncate towards zero
                
                numStack.append(res)

        return numStack.pop()
                    


        