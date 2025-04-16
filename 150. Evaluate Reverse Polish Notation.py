class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        pointer = 0
        stack = []
        while pointer < len(tokens):
            if tokens[pointer] == "+":
                stack.append(stack.pop() + stack.pop())
            elif tokens[pointer] == "-":
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append(op1 - op2)
            elif tokens[pointer] == "*":
                stack.append(stack.pop() * stack.pop())
            elif tokens[pointer] == "/":
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append(int(op1 / op2))
            else:
                stack.append(int(tokens[pointer]))
            pointer += 1
        return stack[-1]

        