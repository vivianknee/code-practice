class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        operatorStack = []
        numStack = []
        operators = {"+", "-", "/", "*"}
        res = 0

        if len(tokens) == 1:
            return int(tokens[0])

        for i in range(len(tokens)):
            if tokens[i] not in operators:
                print("digit: " + tokens[i])
                numStack.append(tokens[i])
                print(numStack)
            if len(operatorStack) == 0 and tokens[i] in operators:
                operatorStack.append(tokens[i])
                print("operator: " + tokens[i])
                if len(numStack) > 1:
                    op = operatorStack.pop()
                    second = int(numStack.pop()) #sec in the eq
                    first = int(numStack.pop()) #first in the eq
                    print( str(first) + op + str(second))

                    if op == '+':
                        res = first + second
                    elif op == '-':
                        res = first - second
                    elif op == '*':
                        res = first * second
                    elif op == '/':
                        res = int(first / second)
                        
                numStack.append(str(res))
                print(numStack)

        return res
                    


        